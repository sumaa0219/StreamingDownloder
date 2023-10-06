import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QSplitter, QTextEdit, QPushButton, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5 import QtGui
from zan_live import zanlive


class Communicator(QObject):
    progressChanged = pyqtSignal(str)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.domain = ""
        self.mainSpliter = QSplitter()
        self.leftSpliter = QSplitter(Qt.Vertical)
        self.rightSpliter = QWebEngineView()
        self.rightSpliter.setFixedSize(800, 600)
        self.mainSpliter.addWidget(self.leftSpliter)
        self.mainSpliter.addWidget(self.rightSpliter)
        # self.mainSpliter.setOrientation(1)

        self.left_URL_Grid = QSplitter(Qt.Vertical)
        self.URL_youtube = QPushButton("Youtube(要望が多ければ)")
        self.URL_youtube.clicked.connect(lambda:
                                         self.select_pages("https://youtube.com"))
        self.URL_zan = QPushButton("Zan-live")
        self.URL_zan.clicked.connect(lambda:
                                     self.select_pages("https://zan-live.com"))
        self.left_URL_Grid.addWidget(self.URL_youtube)
        self.left_URL_Grid.addWidget(self.URL_zan)
        self.leftSpliter.addWidget(self.left_URL_Grid)

        self.left_button = QPushButton("ダウンロード")
        self.left_button.clicked.connect(self.show_download_dialog)
        self.leftSpliter.addWidget(self.left_button)

        self.text_edit = QTextEdit(self)
        self.leftSpliter.addWidget(self.text_edit)

        self.communicator = Communicator()
        self.communicator.progressChanged.connect(self.update_progress)
        sys.stdout = self
        sys.stderr = self

        self.rightSpliter.setUrl(QUrl('https://google.com'))
        # self.rightSpliter.setUrl(
        #     QUrl('https://www.zan-live.com/ja/live/play/2696/1422'))
        self.rightSpliter.settings().setAttribute(
            QWebEngineSettings.JavascriptEnabled, True)
        self.setCentralWidget(self.mainSpliter)
        self.showMaximized()

        # cokkie
        self.cookie_store = self.rightSpliter.page().profile().cookieStore()

        # Cookieの変更を監視
        self.cookie_store.cookieAdded.connect(self.cookie_added)

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.rightSpliter.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.rightSpliter.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.rightSpliter.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.rightSpliter.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.rightSpliter.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.rightSpliter.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def cookie_added(self, cookie):
        # Cookieが追加されたときの処理
        name = cookie.name().data().decode()
        value = cookie.value().data().decode()
        domain = ""
        try:
            domain = cookie.domain().data().decode()
        except:
            domain = cookie.domain()

        if self.domain != domain:
            self.domain = domain
            self.cookie_list = []  # 新しいドメインに切り替えたらリストをリセット
        if (name, value) not in self.cookie_list:
            self.cookie_list.append((name, value))

    def select_pages(self, page_url):
        self.rightSpliter.setUrl(QUrl(page_url))

    def show_download_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        self.download_directory = QFileDialog.getExistingDirectory(
            self, "Select Download Directory", options=options)

        if self.download_directory:
            self.download()

    def download(self):
        self.page_cookie = {x[0]: x[1] for x in self.cookie_list}
        if "zan-live" in self.url_bar.text():
            print("zan")
            zan_live.downloadStreamingData(
                self.rightSpliter, self.page_cookie, self.download_directory)

    def update_progress(self, progress):
        print("Progress:", progress)
        self.text_edit.append(f"Progress: {progress}")

    def write(self, text):
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()


zan_live = zanlive()
cookie_list = []
app = QApplication(sys.argv)
QApplication.setApplicationName('Stream Downloader')
window = MainWindow()
window.setFixedSize(1000, 600)
app.exec_()
