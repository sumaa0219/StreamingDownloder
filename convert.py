from pydub import AudioSegment
import os

# 変換前のwavファイルと変換後のファイル名を指定
input_file = "input.wav"
output_file_dil = "convert"


files = os.listdir("wav")

for x in files:
    # オーディオファイルを読み込み
    audio = AudioSegment.from_file(os.path.join("wav", x))

    # 44.1kHzにリサンプリング
    audio = audio.set_frame_rate(44100)

    # モノラルに変換
    audio = audio.set_channels(1)

    # 変換後のファイルを保存
    audio.export(os.path.join(output_file_dil, x), format="wav")

print("変換が完了しました。")
