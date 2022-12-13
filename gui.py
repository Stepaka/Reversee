# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Stepan\Desktop\игститут\СПБПУ\reversee\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1682, 1204)
        MainWindow.setMinimumSize(QtCore.QSize(1682, 1204))
        MainWindow.setMaximumSize(QtCore.QSize(1682, 1204))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 70, 1731, 1131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background-color: #1F3E26;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.tableWidget = QtWidgets.QTableWidget(self.Main)
        self.tableWidget.setGeometry(QtCore.QRect(870, 560, 451, 431))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"background-color: #1E2F23;\n"
"}QListWidget{\n"
"background-color: #1E2F23;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Main)
        self.tableWidget_2.setGeometry(QtCore.QRect(350, 560, 451, 431))
        self.tableWidget_2.setStyleSheet("QTableWidget{\n"
"background-color: #1E2F23;\n"
"}QListWidget{\n"
"background-color: #1E2F23;\n"
"}")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.groupBox_game = QtWidgets.QGroupBox(self.Main)
        self.groupBox_game.setGeometry(QtCore.QRect(350, 80, 451, 431))
        self.groupBox_game.setStyleSheet("QGroupBox{\n"
"background-color: #1E2F23;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"}")
        self.groupBox_game.setTitle("")
        self.groupBox_game.setObjectName("groupBox_game")
        self.find_game = QtWidgets.QPushButton(self.groupBox_game)
        self.find_game.setEnabled(True)
        self.find_game.setGeometry(QtCore.QRect(50, 40, 351, 71))
        self.find_game.setAcceptDrops(False)
        self.find_game.setObjectName("find_game")
        self.create_game = QtWidgets.QPushButton(self.groupBox_game)
        self.create_game.setGeometry(QtCore.QRect(50, 130, 351, 71))
        self.create_game.setObjectName("create_game")
        self.friend_game = QtWidgets.QPushButton(self.groupBox_game)
        self.friend_game.setGeometry(QtCore.QRect(50, 220, 351, 71))
        self.friend_game.setObjectName("friend_game")
        self.computer_game = QtWidgets.QPushButton(self.groupBox_game)
        self.computer_game.setGeometry(QtCore.QRect(50, 310, 351, 71))
        self.computer_game.setObjectName("computer_game")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.Main)
        self.tableWidget_7.setGeometry(QtCore.QRect(870, 80, 451, 431))
        self.tableWidget_7.setStyleSheet("QTableWidget{\n"
"background-color: #1E2F23;\n"
"}QListWidget{\n"
"background-color: #1E2F23;\n"
"}")
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.textEdit_8 = QtWidgets.QTextEdit(self.Main)
        self.textEdit_8.setGeometry(QtCore.QRect(880, 100, 431, 61))
        self.textEdit_8.setStyleSheet("background-color: #1E2F23;border: 0px;")
        self.textEdit_8.setObjectName("textEdit_8")
        self.board_size = QtWidgets.QSpinBox(self.Main)
        self.board_size.setGeometry(QtCore.QRect(1130, 230, 151, 41))
        self.board_size.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.board_size.setStyleSheet("background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;")
        self.board_size.setObjectName("board_size")
        self.textEdit_9 = QtWidgets.QTextEdit(self.Main)
        self.textEdit_9.setGeometry(QtCore.QRect(910, 230, 191, 41))
        self.textEdit_9.setStyleSheet("background-color: #1E2F23;border: 0px;")
        self.textEdit_9.setObjectName("textEdit_9")
        self.stackedWidget.addWidget(self.Main)
        self.Game = QtWidgets.QWidget()
        self.Game.setStyleSheet("QGroupBox {\n"
"background: #000000;\n"
"}\n"
"QGrindLayout {\n"
"background: #000000;\n"
"}\n"
"QPushButton {\n"
"background: #B39C4D;\n"
"  text-align: center;\n"
"}\n"
"")
        self.Game.setObjectName("Game")
        self.game_board = QtWidgets.QGroupBox(self.Game)
        self.game_board.setGeometry(QtCore.QRect(460, 140, 750, 750))
        self.game_board.setStyleSheet("")
        self.game_board.setTitle("")
        self.game_board.setObjectName("game_board")
        self.gridLayoutWidget = QtWidgets.QWidget(self.game_board)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 751, 751))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget.addWidget(self.Game)
        self.Education = QtWidgets.QWidget()
        self.Education.setObjectName("Education")
        self.groupBox_game_7 = QtWidgets.QGroupBox(self.Education)
        self.groupBox_game_7.setGeometry(QtCore.QRect(360, 80, 1131, 771))
        self.groupBox_game_7.setStyleSheet("QGroupBox{\n"
"background-color: #1E2F23;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"QTextEdit{\n"
"background-color: #1E2F23;\n"
"border: 0px\n"
"}")
        self.groupBox_game_7.setTitle("")
        self.groupBox_game_7.setObjectName("groupBox_game_7")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_game_7)
        self.textEdit_7.setGeometry(QtCore.QRect(80, 40, 971, 711))
        self.textEdit_7.setObjectName("textEdit_7")
        self.stackedWidget.addWidget(self.Education)
        self.Friends = QtWidgets.QWidget()
        self.Friends.setObjectName("Friends")
        self.groupBox_game_8 = QtWidgets.QGroupBox(self.Friends)
        self.groupBox_game_8.setGeometry(QtCore.QRect(400, 50, 861, 911))
        self.groupBox_game_8.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox_game_8.setStyleSheet("QGroupBox{\n"
"background-color: #1E2F23;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"QTextEdit{\n"
"background-color: #1E2F23;\n"
"border: 0px\n"
"}")
        self.groupBox_game_8.setTitle("")
        self.groupBox_game_8.setObjectName("groupBox_game_8")
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox_game_8)
        self.textEdit_10.setGeometry(QtCore.QRect(80, 40, 181, 87))
        self.textEdit_10.setObjectName("textEdit_10")
        self.table_friends = QtWidgets.QTableWidget(self.groupBox_game_8)
        self.table_friends.setGeometry(QtCore.QRect(90, 350, 691, 451))
        self.table_friends.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.table_friends.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_friends.setStyleSheet(".QTableWidget{    \n"
"display: inline-block;\n"
"background-color: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 24px;\n"
"}\n"
"")
        self.table_friends.setAlternatingRowColors(False)
        self.table_friends.setRowCount(0)
        self.table_friends.setColumnCount(0)
        self.table_friends.setObjectName("table_friends")
        self.table_friends.horizontalHeader().setVisible(False)
        self.table_friends.horizontalHeader().setCascadingSectionResizes(False)
        self.table_friends.horizontalHeader().setHighlightSections(False)
        self.table_friends.horizontalHeader().setSortIndicatorShown(False)
        self.table_friends.horizontalHeader().setStretchLastSection(False)
        self.table_friends.verticalHeader().setVisible(False)
        self.table_friends.verticalHeader().setHighlightSections(False)
        self.table_friends.verticalHeader().setSortIndicatorShown(False)
        self.table_friends.verticalHeader().setStretchLastSection(False)
        self.line_find = QtWidgets.QLineEdit(self.groupBox_game_8)
        self.line_find.setGeometry(QtCore.QRect(90, 220, 691, 61))
        self.line_find.setObjectName("line_find")
        self.stackedWidget.addWidget(self.Friends)
        self.Registration = QtWidgets.QWidget()
        self.Registration.setObjectName("Registration")
        self.groupBox_game_9 = QtWidgets.QGroupBox(self.Registration)
        self.groupBox_game_9.setGeometry(QtCore.QRect(520, 70, 661, 831))
        self.groupBox_game_9.setStyleSheet("QGroupBox{\n"
"background-color: #1E2F23;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: #FFFFFF;\n"
"background: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"font-size: 20px;\n"
"}\n"
"QTextEdit{\n"
"color: #FFFFFF;\n"
"background-color: #1E2F23;\n"
"border: 0px;\n"
"}")
        self.groupBox_game_9.setTitle("")
        self.groupBox_game_9.setObjectName("groupBox_game_9")
        self.Registration_but = QtWidgets.QPushButton(self.groupBox_game_9)
        self.Registration_but.setGeometry(QtCore.QRect(80, 610, 491, 71))
        self.Registration_but.setObjectName("Registration_but")
        self.line_login_2 = QtWidgets.QLineEdit(self.groupBox_game_9)
        self.line_login_2.setGeometry(QtCore.QRect(80, 230, 491, 61))
        self.line_login_2.setObjectName("line_login_2")
        self.line_password_reg = QtWidgets.QLineEdit(self.groupBox_game_9)
        self.line_password_reg.setGeometry(QtCore.QRect(80, 380, 491, 61))
        self.line_password_reg.setStyleSheet("")
        self.line_password_reg.setText("")
        self.line_password_reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password_reg.setObjectName("line_password_reg")
        self.textEdit_11 = QtWidgets.QTextEdit(self.groupBox_game_9)
        self.textEdit_11.setGeometry(QtCore.QRect(80, 40, 321, 87))
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.groupBox_game_9)
        self.textEdit_12.setGeometry(QtCore.QRect(80, 180, 491, 41))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.groupBox_game_9)
        self.textEdit_13.setGeometry(QtCore.QRect(80, 330, 491, 41))
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.groupBox_game_9)
        self.textEdit_14.setGeometry(QtCore.QRect(80, 460, 491, 41))
        self.textEdit_14.setObjectName("textEdit_14")
        self.line_password_reg_2 = QtWidgets.QLineEdit(self.groupBox_game_9)
        self.line_password_reg_2.setGeometry(QtCore.QRect(80, 510, 491, 61))
        self.line_password_reg_2.setStyleSheet("")
        self.line_password_reg_2.setText("")
        self.line_password_reg_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password_reg_2.setObjectName("line_password_reg_2")
        self.login_but_wind = QtWidgets.QPushButton(self.groupBox_game_9)
        self.login_but_wind.setGeometry(QtCore.QRect(80, 750, 71, 31))
        self.login_but_wind.setStyleSheet("\n"
"QPushButton {\n"
"  background-color: #1E2F23;\n"
"  color: #FCD655;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"border: 0px;\n"
"}")
        self.login_but_wind.setObjectName("login_but_wind")
        self.stackedWidget.addWidget(self.Registration)
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.groupBox_game_4 = QtWidgets.QGroupBox(self.Login)
        self.groupBox_game_4.setGeometry(QtCore.QRect(540, 70, 661, 721))
        self.groupBox_game_4.setStyleSheet("QGroupBox{\n"
"background-color: #1E2F23;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: #FFFFFF;\n"
"background: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"font-size: 20px;\n"
"}\n"
"QTextEdit{\n"
"color: #FFFFFF;\n"
"background-color: #1E2F23;\n"
"border: 0px;\n"
"}")
        self.groupBox_game_4.setTitle("")
        self.groupBox_game_4.setObjectName("groupBox_game_4")
        self.Login_but = QtWidgets.QPushButton(self.groupBox_game_4)
        self.Login_but.setGeometry(QtCore.QRect(80, 490, 491, 71))
        self.Login_but.setObjectName("Login_but")
        self.line_login = QtWidgets.QLineEdit(self.groupBox_game_4)
        self.line_login.setGeometry(QtCore.QRect(80, 230, 491, 61))
        self.line_login.setObjectName("line_login")
        self.line_password = QtWidgets.QLineEdit(self.groupBox_game_4)
        self.line_password.setGeometry(QtCore.QRect(80, 390, 491, 61))
        self.line_password.setStyleSheet("")
        self.line_password.setText("")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_game_4)
        self.textEdit.setGeometry(QtCore.QRect(80, 40, 321, 87))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_game_4)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 180, 491, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_game_4)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 340, 491, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.registration_but_wind = QtWidgets.QPushButton(self.groupBox_game_4)
        self.registration_but_wind.setGeometry(QtCore.QRect(70, 650, 151, 31))
        self.registration_but_wind.setStyleSheet("\n"
"QPushButton {\n"
"  background-color: #1E2F23;\n"
"  color: #FCD655;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"border: 0px;\n"
"}")
        self.registration_but_wind.setObjectName("registration_but_wind")
        self.save_me = QtWidgets.QCheckBox(self.groupBox_game_4)
        self.save_me.setGeometry(QtCore.QRect(70, 590, 181, 51))
        self.save_me.setStyleSheet(" display: inline-block;\n"
"  border-radius: 4px;\n"
"background-color: #1E2F23;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  padding: 10px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;")
        self.save_me.setObjectName("save_me")
        self.stackedWidget.addWidget(self.Login)
        self.Profile = QtWidgets.QWidget()
        self.Profile.setObjectName("Profile")
        self.groupBox_game_5 = QtWidgets.QGroupBox(self.Profile)
        self.groupBox_game_5.setGeometry(QtCore.QRect(400, 50, 861, 911))
        self.groupBox_game_5.setStyleSheet("QGroupBox{\n"
"background-color: #1E2F23;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"QTextEdit{\n"
"background-color: #1E2F23;\n"
"border: 0px\n"
"}")
        self.groupBox_game_5.setTitle("")
        self.groupBox_game_5.setObjectName("groupBox_game_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_game_5)
        self.textEdit_4.setGeometry(QtCore.QRect(80, 40, 321, 87))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_game_5)
        self.textEdit_5.setGeometry(QtCore.QRect(350, 230, 101, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox_game_5)
        self.textEdit_6.setGeometry(QtCore.QRect(350, 290, 81, 41))
        self.textEdit_6.setObjectName("textEdit_6")
        self.groupBox_game_6 = QtWidgets.QGroupBox(self.groupBox_game_5)
        self.groupBox_game_6.setGeometry(QtCore.QRect(80, 410, 721, 141))
        self.groupBox_game_6.setStyleSheet("QGroupBox{\n"
"background-color: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #B39C4D;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: #2A382F;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"QTextEdit{\n"
"background-color: #1E2F23;\n"
"border: 0px\n"
"}")
        self.groupBox_game_6.setTitle("")
        self.groupBox_game_6.setObjectName("groupBox_game_6")
        self.user_img = QtWidgets.QLineEdit(self.groupBox_game_5)
        self.user_img.setGeometry(QtCore.QRect(80, 140, 200, 200))
        self.user_img.setStyleSheet("")
        self.user_img.setObjectName("user_img")
        self.user_nick = QtWidgets.QTextEdit(self.groupBox_game_5)
        self.user_nick.setGeometry(QtCore.QRect(350, 150, 261, 61))
        self.user_nick.setStyleSheet("  color: #FCD655;\n"
"  text-align: center;\n"
"  font-size: 35px;")
        self.user_nick.setObjectName("user_nick")
        self.textEdit_rating = QtWidgets.QTextEdit(self.groupBox_game_5)
        self.textEdit_rating.setGeometry(QtCore.QRect(470, 230, 121, 41))
        self.textEdit_rating.setStyleSheet("  color: #FCD655;\n"
"  text-align: center;\n"
"  font-size: 20px;")
        self.textEdit_rating.setObjectName("textEdit_rating")
        self.textEdit_place = QtWidgets.QTextEdit(self.groupBox_game_5)
        self.textEdit_place.setGeometry(QtCore.QRect(470, 290, 291, 41))
        self.textEdit_place.setStyleSheet("  color: #FCD655;\n"
"  text-align: center;\n"
"  font-size: 20px;")
        self.textEdit_place.setObjectName("textEdit_place")
        self.exit = QtWidgets.QPushButton(self.groupBox_game_5)
        self.exit.setGeometry(QtCore.QRect(30, 840, 151, 31))
        self.exit.setStyleSheet("\n"
"QPushButton {\n"
"  background-color: #1E2F23;\n"
"  color: #FCD655;\n"
"  text-align: center;\n"
"  font-size: 22px;\n"
"border: 0px;\n"
"}")
        self.exit.setObjectName("exit")
        self.stackedWidget.addWidget(self.Profile)
        self.groupBox_main = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_main.setGeometry(QtCore.QRect(-10, 0, 1701, 81))
        self.groupBox_main.setStyleSheet("QGroupBox{\n"
"background: #1E2F23;\n"
"mix-blend-mode: normal;\n"
"border: 1px solid #B39C4D;\n"
"}\n"
"\n"
"QPushButton {\n"
"    display: inline-block;\n"
"  background-color: #1E2F23;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 24px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;\n"
"}\n"
"\n"
"  \n"
"")
        self.groupBox_main.setTitle("")
        self.groupBox_main.setObjectName("groupBox_main")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 0, 431, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.game_but = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_but.sizePolicy().hasHeightForWidth())
        self.game_but.setSizePolicy(sizePolicy)
        self.game_but.setShortcut("")
        self.game_but.setObjectName("game_but")
        self.horizontalLayout.addWidget(self.game_but)
        self.education_but = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.education_but.sizePolicy().hasHeightForWidth())
        self.education_but.setSizePolicy(sizePolicy)
        self.education_but.setObjectName("education_but")
        self.horizontalLayout.addWidget(self.education_but)
        self.main_but = QtWidgets.QPushButton(self.groupBox_main)
        self.main_but.setGeometry(QtCore.QRect(40, 10, 211, 61))
        self.main_but.setStyleSheet("  font-size: 36px;")
        self.main_but.setObjectName("main_but")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.groupBox_main)
        self.stackedWidget_2.setGeometry(QtCore.QRect(830, 0, 891, 71))
        self.stackedWidget_2.setStyleSheet("background: #1E2F23;")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.login_but = QtWidgets.QPushButton(self.page_login)
        self.login_but.setGeometry(QtCore.QRect(670, 0, 151, 81))
        self.login_but.setObjectName("login_but")
        self.stackedWidget_2.addWidget(self.page_login)
        self.page_user = QtWidgets.QWidget()
        self.page_user.setObjectName("page_user")
        self.profile_but = QtWidgets.QPushButton(self.page_user)
        self.profile_but.setGeometry(QtCore.QRect(490, 0, 211, 81))
        self.profile_but.setStyleSheet("  color: #FCD655;\n"
"  text-align: right;")
        self.profile_but.setText("")
        self.profile_but.setObjectName("profile_but")
        self.profile_2_but = QtWidgets.QPushButton(self.page_user)
        self.profile_2_but.setGeometry(QtCore.QRect(730, 0, 81, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_2_but.sizePolicy().hasHeightForWidth())
        self.profile_2_but.setSizePolicy(sizePolicy)
        self.profile_2_but.setStyleSheet("border-radius: 160px;")
        self.profile_2_but.setText("")
        self.profile_2_but.setIconSize(QtCore.QSize(80, 80))
        self.profile_2_but.setObjectName("profile_2_but")
        self.friends_but = QtWidgets.QPushButton(self.page_user)
        self.friends_but.setGeometry(QtCore.QRect(0, 0, 198, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.friends_but.sizePolicy().hasHeightForWidth())
        self.friends_but.setSizePolicy(sizePolicy)
        self.friends_but.setObjectName("friends_but")
        self.stackedWidget_2.addWidget(self.page_user)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1682, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reversee"))
        self.find_game.setText(_translate("MainWindow", "НАЙТИ ИГРУ"))
        self.create_game.setText(_translate("MainWindow", "СОЗДАТЬ ИГРУ"))
        self.friend_game.setText(_translate("MainWindow", "ИГРА С ДРУГОМ"))
        self.computer_game.setText(_translate("MainWindow", "ИГРА С КОМПЬЮТЕРОМ"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Параметры игры</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">Размер доски:</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Ход игры </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Две золотые и две черные фишки помещены вцентр игрового поля так, как показано на рисунке. Начинают золотые, игрок ходит одной из фишекпо игровому полю. Вы должны перемещать каждую фишку по игровому полю так, чтобы он прилегал как минимум кодной фишке противника. Окруженные фишки – это те фишки, к которым по прямойлинии по вертикали, горизонтали или диагонали прилегает фишка противника. Когда одна из фишек окружена двумя фишками противника, то фишка первого игрокапереворачивается и становится фишкой второго. Если вы поместили свои фишки настолько удачно, что они окружают фишки противника более чемв одном направлении сразу, вы можете перевернуть все эти фишки сразу, превратив их в фишкисвоего цвета. Если игрок не в состоянии переместить фишки согласно правилам, он пропускает ход, и ходпереход к его противнику. Если у игрока уже нет фишек во время хода, он может взять одну усвоего противника. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Конец игры</span><span style=\" font-size:24pt; color:#ffffff;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Игра заканчивается, когда на доске оказываются все 64 фишки или, когда ни один из игроков неможет сделать ход так, чтобы прилегать к фишке соперника. Побеждает игрок с наибольшим количеством фишек своего цвета. В случае равного количествафишек, побеждает игрок, начавший игру вторым.</span></p></body></html>"))
        self.textEdit_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#ffffff;\">Друзья</span></p></body></html>"))
        self.Registration_but.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.textEdit_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#ffffff;\">Регистрация</span></p></body></html>"))
        self.textEdit_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Логин</span></p></body></html>"))
        self.textEdit_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Пароль</span></p></body></html>"))
        self.textEdit_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Повторите пароль</span></p></body></html>"))
        self.login_but_wind.setText(_translate("MainWindow", "Войти"))
        self.Login_but.setText(_translate("MainWindow", "ВОЙТИ"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#ffffff;\">Войти</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Логин</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Пароль</span></p></body></html>"))
        self.registration_but_wind.setText(_translate("MainWindow", "Регистрация"))
        self.save_me.setText(_translate("MainWindow", "Запомнить меня"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#ffffff;\">Профиль</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Рейтинг:</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Место:</span></p></body></html>"))
        self.user_nick.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.textEdit_rating.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.textEdit_place.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.game_but.setText(_translate("MainWindow", "ИГРА"))
        self.education_but.setText(_translate("MainWindow", "ОБУЧЕНИЕ"))
        self.main_but.setText(_translate("MainWindow", "REVERSEE"))
        self.login_but.setText(_translate("MainWindow", "ВОЙТИ"))
        self.friends_but.setText(_translate("MainWindow", "ДРУЗЬЯ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
