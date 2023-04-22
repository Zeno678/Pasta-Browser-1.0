import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a QLineEdit widget for entering URLs
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate)

        # Create a QWebEngineView widget for displaying web pages
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.browser.urlChanged.connect(self.update_urlbar)

        # Add the widgets to the main window
        self.setCentralWidget(self.browser)
        self.addToolBar(self.create_toolbar())
        self.statusBar()

        # Set the window properties
        self.setWindowTitle("Pastabrowser")
        self.setWindowIcon(QIcon("icon.png"))

    def create_toolbar(self):
        # Create a toolbar with buttons for navigating
        toolbar = QToolBar()
        back_button = QAction("Back", self)
        back_button.triggered.connect(self.browser.back)
        toolbar.addAction(back_button)
        forward_button = QAction("Forward", self)
        forward_button.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_button)
        reload_button = QAction("Reload", self)
        reload_button.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_button)
        home_button = QAction("Home", self)
        home_button.triggered.connect(self.navigate_home)
        toolbar.addAction(home_button)
        toolbar.addSeparator()
        toolbar.addWidget(self.urlbar)
        return toolbar

    def navigate(self):
        # Navigate to the URL entered in the QLineEdit widget
        url = self.urlbar.text()
        self.browser.setUrl(QUrl(url))

    def navigate_home(self):
        # Navigate to the home page (in this case, Google)
        self.browser.setUrl(QUrl("http://www.google.com"))

    def update_urlbar(self, url):
        # Update the URL displayed in the QLineEdit widget
        self.urlbar.setText(url.toString())

    def keyPressEvent(self, event):
        # Allow the user to enter fullscreen mode by pressing F11
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
        else:
            super(MainWindow, self).keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
