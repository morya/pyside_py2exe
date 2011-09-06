#coding:utf-8

import sys
from PySide import QtGui
from PySide import QtNetwork
from PySide import QtWebKit
from mywebview import MyWebView

class Mainwin( QtGui.QMainWindow ):
    def __init__( self, title = "WindowTitle" ):
        super( Mainwin, self ).__init__()
        self.setWindowTitle( title )


def main():
    app = QtGui.QApplication( sys.argv )
    mw = Mainwin( "mainwindow" )
    mw.show()
    app.exec_()

if __name__ == '__main__':
    main()
