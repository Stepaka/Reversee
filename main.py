import os

from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PIL import Image, ImageDraw
from Profile import Profile
from gui import Ui_MainWindow
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main)

        self.ui.main_but.clicked.connect(self.main)
        self.ui.game_but.clicked.connect(self.main)
        self.ui.find_game.clicked.connect(self.game)
        self.ui.create_game.clicked.connect(self.game)
        self.ui.friends_but.clicked.connect(self.friends)
        self.ui.login_but.clicked.connect(self.login_window)
        self.ui.education_but.clicked.connect(self.education)
        self.ui.Login_but.clicked.connect(self.login)
        self.ui.profile_but.clicked.connect(self.profile)
        self.ui.profile_2_but.clicked.connect(self.profile)

        self.person = Profile('admin', '123', 'user.png', '2456', '1')
        self.list_person=[]
        self.person1 = Profile('FIRST', '123', 'who.png', '1999', '2')
        self.person2 = Profile('SECOSECONDSECONDSECONDSSECONDECONDSSECONDECONDND', '123', 'who.png', '562', '3')
        self.person3 = Profile('__ALFA__', '123', 'who.png', '0', '5')
        self.person4 = Profile('MPDDS', '123', 'who.png', '125', '4')

        self.list_person.append(self.person1)
        self.list_person.append(self.person2)
        self.list_person.append(self.person3)
        self.list_person.append(self.person4)


        self.ui.board_size.setValue(8)
        self.ui.board_size.setMinimum(6)
        self.ui.board_size.setMaximum(18)
        self.ui.board_size.setSingleStep(2)

    def show(self):
        self.main_win.show()

    def main(self):
        self.game_end()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main)

    def game(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Game)
        self.crate_board()

        self.pre_turn(self.ui.gridLayout_4.itemAt(self.cols * (self.cols / 2 - 1) + (self.cols / 2 - 1)).widget(), True)
        self.pre_turn(self.ui.gridLayout_4.itemAt(self.cols * (self.cols / 2 - 1) + (self.cols / 2)).widget(), False)
        self.pre_turn(self.ui.gridLayout_4.itemAt(self.cols * (self.cols / 2) + (self.cols / 2 - 1)).widget(), False)
        self.pre_turn(self.ui.gridLayout_4.itemAt(self.cols * (self.cols / 2) + (self.cols / 2)).widget(), True)


    def crate_board(self):
        self.counter = 0
        self.cols = int(self.ui.board_size.text())
        self.btns = self.cols ** 2  # количество кнопок
        d = {k: v for k, v in [[f'{i}', f'Item{i}'] for i in range(self.btns)]}
        lst = d
        for i, v in enumerate(lst):
            # btn = QPushButton(v)  # ,objectName=v
            btn = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
            btn.setSizePolicy(sizePolicy)
            btn.clicked.connect(self.turn)
            self.ui.gridLayout_4.addWidget(btn, i // self.cols + 1, i % self.cols + 1)

    def game_end(self):
        for i in range(self.ui.gridLayout_4.count()):
            self.ui.gridLayout_4.itemAt(i).widget().deleteLater()

    def login_window(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)

    def login(self):
        if self.ui.line_login.text() and self.ui.line_password.text():
            if self.ui.line_login.text() == self.person.name and self.ui.line_password.text() == self.person.password:
                self.ui.profile_but.setText(self.person.name)
                self.ui.profile_2_but.setStyleSheet(f'border-image: url({self.person.path});')
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_user)
                self.ui.stackedWidget.setCurrentWidget(self.ui.Main)
                # self.ui.textEdit_rating_2.setText(self.person.rating)

    def friends(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Friends)
        self.ui.table_friends.setColumnCount(4)
        self.ui.table_friends.setRowCount(len(self.list_person))
        
        self.ui.table_friends.verticalHeader().setDefaultSectionSize(110)
        self.ui.table_friends.horizontalHeader().setDefaultSectionSize(100)
        self.ui.table_friends.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.table_friends.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.table_friends.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.ui.table_friends.alternatingRowColors()


        for i in range(len(self.list_person)):
            btn_img = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            btn_img.setIcon(QIcon(self.list_person[i].path))
            btn_img.setIconSize(QSize(100, 100))

            btn_img.clicked.connect(lambda state, x=self.list_person[i]: self.profile_users(x))

            btn_invite = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            btn_invite.setText('Пригласить')
            btn_invite.setStyleSheet('.QPushButton {  background-color: #B39C4D;color: #FFFFFF; text-align: center; '
                                     'font-size: 22px;}')
            self.ui.table_friends.setCellWidget(i, 0, btn_img)
            self.ui.table_friends.setItem(i, 1, self.create_item(self.list_person[i].name))
            self.ui.table_friends.setItem(i, 2, self.create_item(self.list_person[i].rating))
            self.ui.table_friends.setCellWidget(i, 3, btn_invite)

            self.ui.table_friends.resizeColumnsToContents()
    def create_item(self, string ):
        item = QtWidgets.QTableWidgetItem(string)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        return item
    def profile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Profile)
        self.ui.user_img.setStyleSheet(f'border-image: url({self.person.path});')
        self.ui.textEdit_rating.setText(self.person.rating)
        self.ui.textEdit_place.setText(self.person.place)
        self.ui.user_nick.setText(self.person.name)

    def profile_users(self, user):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Profile)
        self.ui.user_img.setStyleSheet(f'border-image: url({user.path});')
        self.ui.textEdit_rating.setText(user.rating)
        self.ui.textEdit_place.setText(user.place)
        self.ui.user_nick.setText(user.name)
    def education(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Education)

    def turn(self):
        sender = self.sender()
        if isinstance(sender, QPushButton):
            if self.counter % 2==0:
                sender.setStyleSheet('.QPushButton {border-image: url(w.png);}')
            else: sender.setStyleSheet('.QPushButton {border-image: url(b.png);}')
            sender.setEnabled(False)
            self.counter+=1

    def pre_turn(self, but, color):
        if color:
            but.setStyleSheet('.QPushButton {border-image: url(w.png);}')
        else:
            but.setStyleSheet('.QPushButton {border-image: url(b.png);}')


        # print(self.ui.gridLayout_4.itemAt(id).widget())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_min = MainWindow()
    main_min.show()
    sys.exit(app.exec_())
