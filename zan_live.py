import os
import requests
from urllib.parse import urlsplit
import threading
import m3u8
import decryp
import re
import ffmpeg
import shutil
import subprocess

dc = decryp.decryp()


class zanlive():

    def __init__(self):
        self.links = []
        self.file_name = ""
        self.cookie = {}
        self.filePath = ""
        self.baseURL = ""
        self.progress = ""
        self.pathArry = []

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def show_progress(self):
        return self.progress

    def getm3u8(self, window):
        print("searching m3u8 files URL......")
        # ページの読み込みが成功した場合
        window.page().toHtml(lambda html: extract_m3u8_links(html))

        def extract_m3u8_links(html):
            # HTML内のm3u8ファイルへのリンクを抽出
            # ここでは単純に"http"で始まるリンクを抽出する例を示しています
            start = 0
            while True:
                start = html.find("http", start)
                if start == -1:
                    break
                end = html.find('"', start)
                link = html[start:end]
                if link.endswith(".m3u8"):
                    self.links.append(link)
                start = end

    def download_m3u8(self, window):
        print("start to download m3u8....")

        def save_m3u8():
            for url in self.links:
                # URLを分割して最後の要素を取得
                self.url = url
                url_path = urlsplit(url).path
                self.parts = url_path.split("/")
                self.file_name = self.parts[-1]
                print(url, self.file_name)
                r = requests.get(url=url, cookies=self.cookie)
                self.filePath = os.path.join(path, self.file_name)
                print("path:", self.filePath)
                with open(self.filePath, 'wb') as saveFile:
                    saveFile.write(r.content)
            print("succese download m3u8!")

        self.getm3u8(window)
        path = os.path.join("assets", "m3u8")
        self.create_directory(path)

        timer = threading.Timer(1, save_m3u8)  # 2秒後にdelayed_functionを呼び出す
        timer.start()

    def getStreamingm3u8(self, window, cookie):

        def getStreamingURL():
            print("getting streaming URL...")
            global streamingm3u8
            dir_path = os.listdir(os.path.join("assets", "m3u8"))
            self.baseURL = self.links[0].replace(self.file_name, "")
            streamingm3u8 = m3u8.load(
                os.path.join("assets", "m3u8", dir_path[0]))

            url = self.baseURL + streamingm3u8.playlists[0].uri
            url_path = urlsplit(url).path
            parts = url_path.split("/")
            file_name = parts[-1]
            r = requests.get(url=url, cookies=self.cookie)
            filePath = os.path.join("assets", "m3u8", file_name)
            with open(filePath, 'wb') as saveFile:
                saveFile.write(r.content)
            print("succese getting streaming m3u8!")

        self.cookie = cookie
        self.download_m3u8(window)
        # 2秒後にdelayed_functionを呼び出す
        timer = threading.Timer(3, getStreamingURL)
        timer.start()

    def downloadStreamingData(self, window, cookie, download_directory):
        print("starting download")
        self.getStreamingm3u8(window, cookie)
        self.download_directory = download_directory

        def getAES128_key_in(indexm3u8):
            key = indexm3u8.keys[0]
            keyurl = key.uri
            keyiv = key.iv[2:]

            url_path = urlsplit(keyurl).path
            parts = url_path.split("/")
            file_name = parts[-1]
            r = requests.get(url=keyurl, cookies=self.cookie)
            filePath = os.path.join("assets", "key")
            self.create_directory(filePath)
            filePath = os.path.join(filePath, file_name)
            with open(filePath, 'wb') as saveFile:
                saveFile.write(r.content)
            print("succese get key file")

            return (filePath, keyiv)

        def download():
            global streamingm3u8
            indexm3u8 = m3u8.load(os.path.join("assets", "m3u8", "index.m3u8"))
            key, iv = getAES128_key_in(indexm3u8)
            dc.setkey_iv(key, iv)

            for i, segment in enumerate(indexm3u8.segments):
                numAllFiles = i

            for i, segment in enumerate(indexm3u8.segments):
                # tsファイルのパス
                uri = segment.absolute_uri.split("/")[-1]
                BaseURL = re.sub(self.file_name, "", self.url)
                base = urlsplit((streamingm3u8.playlists[0].uri)).path
                url_quality_path = base.split("/")[0]
                URL = BaseURL + url_quality_path+"/" + uri

                path = os.path.join("assets", "video", uri)
                self.create_directory(os.path.dirname(path))

                if os.path.exists(path):
                    pass
                else:
                    r = requests.get(url=URL, cookies=self.cookie)
                    with open(path, 'wb') as saveFile:
                        saveFile.write(r.content)
                self.progress = float(i/numAllFiles*100)
                pro_bar = ('=' * int(self.progress/10)) + \
                    (' ' * (10 - int(self.progress/10)))
                print('\r[{0}] {1}%   ダウンロード完了'.format(
                    pro_bar, round(self.progress, 2)), end='')

            for i, segment in enumerate(indexm3u8.segments):
                uri = segment.absolute_uri.split("/")[-1]
                path = os.path.join("assets", "video", uri)
                outpath = os.path.join("assets", "video_decript", uri)
                ffmpeg_outPath = os.path.join("video_decript", uri)
                self.pathArry.append(ffmpeg_outPath)
                self.create_directory(os.path.dirname(outpath))
                if os.path.exists(outpath):
                    pass
                else:
                    dc.decrypt_file(path, outpath)
                    self.progress = float(i/numAllFiles*100)
                    self.progress = float(i/numAllFiles*100)
                    pro_bar = ('=' * int(self.progress/10)) + \
                        (' ' * (10 - int(self.progress/10)))
                    print('\r[{0}] {1}%   復号完了'.format(
                        pro_bar, round(self.progress, 2)), end='')

            with open(os.path.join("assets", "tmp.txt"), "w") as fp:
                # file 'パス' という形式にする
                lines = [f"file '{line}'" for line in self.pathArry]
                fp.write("\n".join(lines))
            # ffmpegで結合（再エンコードなし
            textPath = os.path.join("assets", "tmp.txt")
            print("\nprossesting ffmpeg. please wait for....")
            ffmpeg.input(textPath, f="concat", safe=0).output(
                os.path.join(self.download_directory, "out.mp4"), c="copy").run()
            shutil.rmtree("assets")
            print("succese!!")
            subprocess.Popen(['explorer', self.download_directory], shell=True)

        timer = threading.Timer(5, download)
        timer.start()
