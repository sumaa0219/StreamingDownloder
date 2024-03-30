import os
from pytube import YouTube  # , Playlist
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import ffmpeg

# YouTube動画をダウンロードする関数


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(90, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton.setFont(font)
        self.radioButton.setIconSize(QtCore.QSize(40, 40))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.clicked.connect(
            lambda: self.display_video_files(Form))
        self.radioButton.clicked.connect(self.disable_audio_buttons)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(400, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.clicked.connect(
            lambda: self.display_audio_files(Form))
        self.radioButton_2.clicked.connect(self.disable_video_buttons)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.download_button = QPushButton("ダウンロード", Form)
        self.download_button.setGeometry(500, 400,  100, 50)
        self.download_button.clicked.connect(
            lambda: self.on_download_button_clicked(Form))

    def retranslateUi(self, Form):
        global videoList, audioList
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "動画ファイル"))
        self.radioButton_2.setText(_translate("Form", "音声ファイル"))

    # 動画ファイルを選択したとき、音声ファイルのボタンを無効化する
    def disable_audio_buttons(self):
        try:
            for button in self.AudioRadiobuttons:
                button.setEnabled(False)
        except:
            pass

    # 音声ファイルを選択したとき、動画ファイルのボタンを無効化する
    def disable_video_buttons(self):
        try:
            for button in self.VideoRadiobuttons:
                button.setEnabled(False)
        except:
            pass

    def display_video_files(self, Form):
        global videoList
        self.VideoRadiobuttons = []
        groupbox = QtWidgets.QGroupBox(Form)
        groupbox.setGeometry(QtCore.QRect(
            80, 60, 220, len(videoList) * 30 + 20))
        for i, file in enumerate(videoList):
            message = str(file.resolution) + " " + \
                str(file.fps) + "fps " + str(file.video_codec)
            radiobutton = QtWidgets.QRadioButton(groupbox)
            radiobutton.setGeometry(QtCore.QRect(10, 10 + i * 30, 151, 31))
            radiobutton.setText(message)
            self.VideoRadiobuttons.append(radiobutton)
            radiobutton.show()
        groupbox.show()

    def display_audio_files(self, Form):
        global audioList
        self.AudioRadiobuttons = []
        groupbox = QtWidgets.QGroupBox(Form)
        groupbox.setGeometry(QtCore.QRect(
            390, 60, 200, len(audioList) * 30 + 20))
        for i, file in enumerate(audioList):
            message = str(file.abr) + " " + str(file.audio_codec)
            radiobutton = QtWidgets.QRadioButton(groupbox)
            radiobutton.setGeometry(QtCore.QRect(10, 10 + i * 30, 151, 31))
            radiobutton.setText(message)
            self.AudioRadiobuttons.append(radiobutton)
            radiobutton.show()
        groupbox.show()

    def on_download_button_clicked(self, Form):

        selected_video = None
        selected_audio = None
        label = QtWidgets.QLabel(Form)
        label.setText("このウィンドウが閉じるまでお待ちください")
        label.setGeometry(300, 200, 300, 30)  # 適切な位置とサイズに設定します
        label.show()

        try:
            for i, button in enumerate(self.VideoRadiobuttons):
                if button.isChecked():
                    selected_video = videoList[i]
                    break
        except:
            pass

        try:
            for i, button in enumerate(self.AudioRadiobuttons):
                if button.isChecked():
                    selected_audio = audioList[i]
                    break
        except:
            pass

        global out_dir, URL
        if selected_video:
            filename = os.path.join(out_dir, selected_video.default_filename)
            selected_video.download(output_path=out_dir, filename="video.mp4")
            yt = YouTube(URL)
            audio_stream = yt.streams.get_audio_only()
            audio_stream.download(output_path=out_dir, filename="audio.mp3")
            # selected_video.get_file_path()
            # print(selected_video.default_filename)
            video_stream = ffmpeg.input(os.path.join(
                out_dir, "video.mp4"))
            audio_stream = ffmpeg.input(os.path.join(
                out_dir, "audio.mp3"))
            # print(filename)
            output = ffmpeg.output(video_stream, audio_stream, filename,
                                   vcodec='copy', acodec='aac', strict='experimental')
            output.run()
            os.remove(os.path.join(
                out_dir, "video.mp4"))
            os.remove(os.path.join(
                out_dir, "audio.mp3"))
            Form.close()
        if selected_audio:
            selected_audio.download(output_path=out_dir)


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


def download(type: str, url: str, output_dir: str):
    global out_dir, URL
    URL = url
    out_dir = output_dir
    if type == "video":
        global videoList, audioList
        videoList, audioList = getVideoFormatFromUrl(url)

    return SubWindow()


def getVideoFormatFromUrl(url):
    yt = YouTube(url)
    # print(yt.streams.all())
    audioList = yt.streams.filter(only_audio=True).all()
    videoList = yt.streams.filter(only_video=True).all()
    return videoList, audioList


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


# if __name__ == "__main__":
#     # youtube_url = input("YouTubeのリンクを入力してください: ")
#     playlist_url = "https://www.youtube.com/watch?v=rTGlK5XB3Ko&list=PL3_NLXp9puXWs19A9mdPXkoQ_WZ4IEBvp&pp=iAQB"

#     # Playlistオブジェクトを作成
#     playlist = Playlist(playlist_url)

#     # 動画のURLをリストに格納
#     video_urls = playlist.video_urls

#     output_directory = "dataset"

#     files = os.listdir("dataset")

#     all = 0
#     for i, x in enumerate(video_urls):
#         all = i

#     filename = []
#     # for i, x in enumerate(video_urls):

#     #     print("downloading", x)
#     #     video_file = download_youtube_video(x, output_directory)
#     #     filename.append(video_file)
#     #     print(f"動画は {video_file} として保存されました。", "進捗", i/all*100)

#     for i, x in enumerate(video_urls):
#         wav_file = convert_to_wav(os.path.join(
#             output_directory, files[i]), output_directory)
#         print(f"動画は {wav_file} として保存されました。", "進捗", i/all*100)

#     # YouTube動画をダウンロード
#     # video_file = download_youtube_video(youtube_url, output_directory)

#     # MP3に変換
#     # mp3_file = convert_to_mp3(os.path.join( output_directory, video_file), output_directory)
#     # mp3_file = convert_to_mp3("output/piano.mp4", output_directory)
#     # wav_file = convert_to_wav(os.path.join(
#     #     output_directory, video_file), output_directory)

#     print(f"動画は {wav_file} として保存されました。")
#     # print(f"MP3は {mp3_file} として保存されました。")
