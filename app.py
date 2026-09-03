import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from tkinter import Tk, filedialog, simpledialog
from urllib.parse import urlparse


def pick_m3u8_url() -> str | None:
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    entered = simpledialog.askstring(
        title="Input m3u8 URL",
        prompt="Enter m3u8 URL (HLS):",
        parent=root,
    )
    root.destroy()
    if not entered:
        return None
    return entered.strip()


def pick_output_file(default_name: str) -> Path | None:
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    selected = filedialog.asksaveasfilename(
        title="Save as",
        defaultextension=".mp4",
        initialfile=default_name,
        filetypes=[("MP4 video", "*.mp4")],
    )
    root.destroy()
    if not selected:
        return None
    return Path(selected)


def build_ffmpeg_command(input_m3u8_url: str, output_mp4: Path) -> list[str]:
    ffmpeg_exe = resolve_ffmpeg_executable()
    if ffmpeg_exe is None:
        raise FileNotFoundError("ffmpeg executable was not found")

    return [
        str(ffmpeg_exe),
        "-y",
        "-protocol_whitelist",
        "http,https,tcp,tls,crypto,file",
        "-i",
        input_m3u8_url,
        "-c",
        "copy",
        str(output_mp4),
    ]


def is_valid_http_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def default_output_name_from_url(url: str) -> str:
    parsed = urlparse(url)
    name = Path(parsed.path).stem
    if not name:
        name = "download"
    return f"{name}.mp4"


def resolve_ffmpeg_executable() -> Path | None:
    # PyInstaller onefile extracts bundled files under _MEIPASS.
    if getattr(sys, "frozen", False):
        meipass = getattr(sys, "_MEIPASS", None)
        if meipass:
            bundled = Path(meipass) / "ffmpeg.exe"
            if bundled.exists():
                return bundled

    local_ffmpeg = Path(__file__).resolve().parent / "ffmpeg.exe"
    if local_ffmpeg.exists():
        return local_ffmpeg

    ffmpeg_on_path = shutil.which("ffmpeg")
    if ffmpeg_on_path:
        return Path(ffmpeg_on_path)
    return None


def download_from_m3u8(input_m3u8_url: str, output_mp4: Path) -> int:
    ffmpeg_exe = resolve_ffmpeg_executable()
    if ffmpeg_exe is None:
        print("Error: ffmpeg is not found in PATH.")
        print("Please place ffmpeg.exe next to the app or install ffmpeg in PATH.")
        return 1

    output_mp4.parent.mkdir(parents=True, exist_ok=True)
    cmd = build_ffmpeg_command(input_m3u8_url, output_mp4)
    print("Starting download...")
    print("ffmpeg:", ffmpeg_exe)
    print("Input :", input_m3u8_url)
    print("Output:", output_mp4)

    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Download failed. ffmpeg exited with code", result.returncode)
        return result.returncode

    print("Done.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Input an m3u8 URL and download it as mp4."
    )
    parser.add_argument("--url", type=str, help="Input m3u8 URL")
    parser.add_argument("--output", type=Path, help="Output mp4 file path")
    args = parser.parse_args()

    input_m3u8_url = args.url or pick_m3u8_url()
    if input_m3u8_url is None:
        print("Canceled: no m3u8 URL entered.")
        return 1

    if not is_valid_http_url(input_m3u8_url):
        print("Error: URL must start with http:// or https://")
        return 1

    default_name = default_output_name_from_url(input_m3u8_url)
    output_mp4 = args.output or pick_output_file(default_name)
    if output_mp4 is None:
        print("Canceled: no output file selected.")
        return 1

    return download_from_m3u8(input_m3u8_url, output_mp4)


if __name__ == "__main__":
    sys.exit(main())
