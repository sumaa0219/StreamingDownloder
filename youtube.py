import os
from pytube import YouTube, Playlist
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# YouTube動画をダウンロードする関数


def download_youtube_video(url, output_dir):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path=output_dir)
    return video_stream.default_filename

# MP4をMP3に変換する関数


def convert_to_mp3(input_path, output_dir):
    video_name = os.path.basename(input_path)
    mp3_name = os.path.splitext(video_name)[0] + ".mp3"
    mp3_output_path = os.path.join(output_dir, mp3_name)

    os.system(f"ffmpeg -i {input_path} -q:a 0 -map a {mp3_output_path}")
    return mp3_output_path


def convert_to_wav(input_path, output_dir):
    video_name = os.path.basename(input_path)
    wav_name = os.path.splitext(video_name)[0] + ".wav"
    wav_output_path = os.path.join(output_dir, wav_name)

    os.system(
        f"ffmpeg -i {input_path} -acodec pcm_s16le -ar 44100 -ac 2 {wav_output_path}")
    return wav_output_path


if __name__ == "__main__":
    # youtube_url = input("YouTubeのリンクを入力してください: ")
    playlist_url = "https://www.youtube.com/watch?v=rTGlK5XB3Ko&list=PL3_NLXp9puXWs19A9mdPXkoQ_WZ4IEBvp&pp=iAQB"

    # Playlistオブジェクトを作成
    playlist = Playlist(playlist_url)

    # 動画のURLをリストに格納
    video_urls = playlist.video_urls

    output_directory = "dataset"

    files = os.listdir("dataset")

    all = 0
    for i, x in enumerate(video_urls):
        all = i

    filename = []
    # for i, x in enumerate(video_urls):

    #     print("downloading", x)
    #     video_file = download_youtube_video(x, output_directory)
    #     filename.append(video_file)
    #     print(f"動画は {video_file} として保存されました。", "進捗", i/all*100)

    for i, x in enumerate(video_urls):
        wav_file = convert_to_wav(os.path.join(
            output_directory, files[i]), output_directory)
        print(f"動画は {wav_file} として保存されました。", "進捗", i/all*100)

    # YouTube動画をダウンロード
    # video_file = download_youtube_video(youtube_url, output_directory)

    # MP3に変換
    # mp3_file = convert_to_mp3(os.path.join( output_directory, video_file), output_directory)
    # mp3_file = convert_to_mp3("output/piano.mp4", output_directory)
    # wav_file = convert_to_wav(os.path.join(
    #     output_directory, video_file), output_directory)

    print(f"動画は {wav_file} として保存されました。")
    # print(f"MP3は {mp3_file} として保存されました。")
