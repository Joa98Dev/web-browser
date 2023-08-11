# Importing libraries
from importlib import reload
from json.tool import main
import sys
from tkinter import Button
from turtle import back, bgcolor, color, forward
from webbrowser import BackgroundBrowser
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon

#Browser Structure
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        
        #Here will be the website that'll initialize with the web browser
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        
        #Icon
        self.setWindowIcon(QIcon('icon.ico'))

        #Displayed the QWebEngineView in the central area and maximized
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #Create a Navigation Bar and added to the main window
        navigation_bar = QToolBar()
        self.addToolBar(Qt.BottomToolBarArea, navigation_bar)

        #Back button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)

        #Forward button
        forward_button = QAction('forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        #Reload button
        refresh_button = QAction('Refresh', self)
        refresh_button.triggered.connect(self.browser.reload)  
        navigation_bar.addAction(refresh_button)

        #Home button
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navigation_bar.addAction(home_button)
        
        #Create a URL bar
        self.url_bar = QLineEdit()
        navigation_bar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_url)
        self.browser.urlChanged.connect(self.update_url)

    #Function that add the main webiste url to the url bar
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com/')) 
        
    #Add functionality to the url bar
    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        
    #Function that will update the url displayed in the url bar
    def update_url(self, url_displayed):
        self.url_bar.setText(url_displayed.toString())

#Initialize the browser app
app = QApplication(sys.argv)
#Sets the app's name
QApplication.setApplicationName('Web Browser')
#Initialize with the class MainWindow()
window = MainWindow()
#Start the loop to display the GUI
app.exec_()
