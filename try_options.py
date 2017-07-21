# -*- coding: utf-8 -*-

from PyQt4 import uic
from PyQt4 import QtGui
import sys

qtCreatorFile = "try_options.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MainUI(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(u"组件试验厂")
        a = QtGui.QTableWidgetItem('!!!')
        a.setText('`12')
        #b = self.tableWidget.item(2,2)
        #b.setText('444444')
        b = QtGui.QTableWidgetItem('!!!')
        self.tableWidget.setItem(0, 0, a)
        self.tableWidget.setItem(0, 1, b)
        # a.setText('yyy')
        # self.tableWidget.setItem(2, 2, a)
        self.move_up_button.clicked.connect(self.item_move_up)
        a = self.lineEdit.text().toUtf8().data()


    def item_move_up(self):
        current_cow = self.listWidget.currentRow()
        if current_cow != 0:
            up_qtext = self.listWidget.item(current_cow-1).text()
            current_qtext = self.listWidget.item(current_cow).text()
            self.listWidget.item(current_cow - 1).setText(current_qtext)
            self.listWidget.item(current_cow).setText(up_qtext)
            self.listWidget.setCurrentItem(self.listWidget.item(current_cow - 1))




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())
