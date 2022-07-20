from PyQt5 import QtWidgets, QtGui
from gui import Ui_MainWindow
import requests
import sys, os
import YTS_CLI
import pyperclip as clip
import iso639

class AppUI(Ui_MainWindow):
    sortOptions = {'Title':'title', 'Release Year':'year', 'IMDB Rating':'rating', 'Download Count':'download_count', 'User likes':'like_count', 'Date Added':'date_added'}
    CONNECTED = False
    def __init__(self, MainWindow, networkErrorCallback):
        self.Main = MainWindow
        self.netErr = networkErrorCallback
        self.connect()
        self.setupUi(MainWindow)
        self.setup()

    def connect(self):
        while self.CONNECTED == False:
            temp = YTS_CLI.yts()
            if temp.connected:
                self.CONNECTED = True
                self.YTS = temp
            else:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Critical)
                msgBox.setText('Cannot connect to YTS, please check your network!')
                msgBox.setWindowTitle('ERROR!')
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Cancel)
                if msgBox.exec_() == 4194304 :
                    sys.exit()
                del temp

    def setup(self):
        self.sortBox.addItems(self.sortOptions)
        self.sortOrder.setChecked(True)
        self.searchButton.clicked.connect(self.search)
        self.searchResults.clicked.connect(self.select)
        self.searchText.returnPressed.connect(self.search)
        self.copyMagnet.setEnabled(False)
        self.copyMagnet.clicked.connect(lambda _:clip.copy(self.getmagnet()))
        self.downloadMagnet.setEnabled(False)
        self.downloadMagnet.clicked.connect(self.magnet)
        self.downloadTorrent.setEnabled(False)
        self.downloadTorrent.clicked.connect(self.torrent)

    def search(self):
        try:
            order = 'asc' if self.sortOrder.isChecked() else 'desc'
            sortBy = self.sortOptions[self.sortBox.currentText()]
            self.searchButton.setEnabled(False)
            keyw = self.searchText.text()
            if keyw == '':
                self.showMessageBox('Search box is empty!', 'Error!')
            else:
                self.searchResults.clear()
                self.YTS.search(keyword=keyw, sortBy=sortBy, orderBy=order)
                if self.YTS.countResult != 0:
                    self.showMessageBox(f'{self.YTS.countResult} results found!', 'Search')
                    self.movies = list()
                    self.moviesList = list()
                    for i in self.YTS.moviesList:
                        self.moviesList+=i
                    for i in self.moviesList:
                        self.movies.append(i['title'])
                    self.searchResults.addItems(self.movies)
                else:
                    self.showMessageBox(f"No movies found by '{keyw}'!", 'Alert!')
            self.searchButton.setEnabled(True)
        except Exception as e:
            self.netErr(e)

    def select(self):
        try:
            selected = self.searchResults.currentItem().text()
            print(f'Selected: {selected}')
            self.populateData(self.moviesList[self.movies.index(selected)])
            self.downloadMagnet.setEnabled(True)
            self.copyMagnet.setEnabled(True)
            self.downloadTorrent.setEnabled(True)
        except Exception as e:
            self.netErr(e)

    def populateData(self, movie):
        #cover
        image = QtGui.QImage()
        image.loadFromData(requests.get(movie['medium_cover_image'],allow_redirects=True).content)
        self.movMediumCover.setPixmap(QtGui.QPixmap(image))

        #details
        self.movTitle.setText(movie['title'])
        self.movYear.setText(str(movie['year']))
        self.movIMDB.setText(str(movie['rating']))
        runtime = movie['runtime']
        hrs = runtime//60
        mins = runtime - hrs*60
        self.movRuntime.setText(f'{hrs} hrs {mins} mins')

        genres = ''.join(x+', ' for x in movie['genres'])
        genres = genres[:-2]
        self.movGenre.setText(genres)

        self.movSummary.setHtml(movie['summary'])
        self.movTrailer.setText(f"""<a href="https://youtu.be/{movie['yt_trailer_code']}">Click Me!</a>""")

        lang = iso639.languages.get(alpha2=movie['language'])
        self.movLang.setText(lang.name)
        self.movQualCount.setText(str(len(movie['torrents'])))

        self.movQuals.clear()
        for i in movie['torrents']:
            self.movQuals.addItem(f"{i['quality']} - {i['type']} - {i['size']}")

    def getmagnet(self):
        selected = self.moviesList[self.movies.index(self.searchResults.currentItem().text())]['torrents'][self.movQuals.currentIndex()]['hash']
        return self.YTS.makeMagnet(selected, self.searchResults.currentItem().text())

    def magnet(self):
        os.startfile(self.getmagnet())

    def torrent(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self.Main, 'Save As')
        url = self.moviesList[self.movies.index(self.searchResults.currentItem().text())]['torrents'][self.movQuals.currentIndex()]['url']
        data = requests.get(url,allow_redirects=True).content
        with open(path+'/'+self.searchResults.currentItem().text()+'.torrent','wb+') as f:
            f.write(data)

    def showMessageBox(self, msg, title):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

def networkError(errmsg):
    print(errmsg)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AppUI(MainWindow, networkError)
    MainWindow.show()
    sys.exit(app.exec_())
