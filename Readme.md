# StreamDownloader

## what is this?
A minimal script that lets you input an HLS `.m3u8` URL and download it as `.mp4`.

## requirements
- Python 3.10+
- `ffmpeg.exe` (for bundled build, put it in project root)

## setup
```bash
pip install -r requirements.txt
```

## run
```bash
python app.py
```

1. Input the source `.m3u8` URL.
2. Select where to save the output `.mp4`.
3. The script runs `ffmpeg` and saves the video.

Optional CLI mode:
```bash
python app.py --url "https://example.com/path/index.m3u8" --output "C:\path\to\out.mp4"
```

## build exe
```bash
pyinstaller --onefile --name StreamDownloader --add-binary "ffmpeg.exe;." app.py
```

The executable is created at:
- `dist/StreamDownloader.exe`

Notes:
- The built exe uses bundled `ffmpeg.exe` first.
- If bundled ffmpeg is not present, it falls back to PATH.