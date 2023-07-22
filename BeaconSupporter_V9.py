from PySide2 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 870)
        MainWindow.setStyleSheet("\n"
        "background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_ClearLabelOutput = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_ClearLabelOutput.setGeometry(QtCore.QRect(500, 10, 23, 23))
        self.pushButton_ClearLabelOutput.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_ClearLabelOutput.setObjectName("pushButton_ClearLabelOutput")
        self.verticalLayout_4.addWidget(self.widget_2)
        self.label_Output = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Output.setFont(font)
        self.label_Output.setStyleSheet("background: rgb(25, 25, 25);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "color: rgb(211, 211, 211);\n"
        "border-radius: 10px;")
        self.label_Output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Output.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_Output.setObjectName("label_Output")
        self.verticalLayout_4.addWidget(self.label_Output)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(10, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 10))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_5.setObjectName("widget_5")
        self.label_TempText_2 = QtWidgets.QLabel(self.widget_5)
        self.label_TempText_2.setGeometry(QtCore.QRect(30, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_TempText_2.setFont(font)
        self.label_TempText_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_TempText_2.setObjectName("label_TempText_2")
        self.pushButton_SaveNote = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_SaveNote.setGeometry(QtCore.QRect(430, 15, 75, 23))
        self.pushButton_SaveNote.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_SaveNote.setObjectName("pushButton_SaveNote")
        self.PerforceIcon_4 = QtWidgets.QPushButton(self.widget_5)
        self.PerforceIcon_4.setEnabled(False)
        self.PerforceIcon_4.setGeometry(QtCore.QRect(0, 12, 30, 30))
        font = QtGui.QFont()
        font.setKerning(False)
        self.PerforceIcon_4.setFont(font)
        self.PerforceIcon_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icon5.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PerforceIcon_4.setIcon(icon)
        self.PerforceIcon_4.setIconSize(QtCore.QSize(25, 25))
        self.PerforceIcon_4.setFlat(True)
        self.PerforceIcon_4.setObjectName("PerforceIcon_4")
        self.pushButton_ReadNote = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_ReadNote.setGeometry(QtCore.QRect(340, 15, 75, 23))
        self.pushButton_ReadNote.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_ReadNote.setObjectName("pushButton_ReadNote")
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.textEdit_SS_TempNote = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_SS_TempNote.setGeometry(QtCore.QRect(0, 0, 501, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_SS_TempNote.setFont(font)
        self.textEdit_SS_TempNote.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "")
        self.textEdit_SS_TempNote.setPlaceholderText("")
        self.textEdit_SS_TempNote.setObjectName("textEdit_SS_TempNote")
        self.verticalLayout.addWidget(self.widget_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_PerforceDescription = QtWidgets.QPushButton(self.frame)
        self.pushButton_PerforceDescription.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.pushButton_PerforceDescription.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_PerforceDescription.setObjectName("pushButton_PerforceDescription")
        self.label_PD_ProjectName = QtWidgets.QLabel(self.frame)
        self.label_PD_ProjectName.setGeometry(QtCore.QRect(0, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PD_ProjectName.setFont(font)
        self.label_PD_ProjectName.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PD_ProjectName.setObjectName("label_PD_ProjectName")
        self.label_PD_UserName = QtWidgets.QLabel(self.frame)
        self.label_PD_UserName.setGeometry(QtCore.QRect(0, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PD_UserName.setFont(font)
        self.label_PD_UserName.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PD_UserName.setObjectName("label_PD_UserName")
        self.label_PD_Changes = QtWidgets.QLabel(self.frame)
        self.label_PD_Changes.setGeometry(QtCore.QRect(0, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PD_Changes.setFont(font)
        self.label_PD_Changes.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PD_Changes.setObjectName("label_PD_Changes")
        self.lineEdit_PD_ProjectName = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_PD_ProjectName.setGeometry(QtCore.QRect(190, 70, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_PD_ProjectName.setFont(font)
        self.lineEdit_PD_ProjectName.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_PD_ProjectName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PD_ProjectName.setObjectName("lineEdit_PD_ProjectName")
        self.lineEdit_PD_UserName = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_PD_UserName.setGeometry(QtCore.QRect(190, 40, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_PD_UserName.setFont(font)
        self.lineEdit_PD_UserName.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_PD_UserName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PD_UserName.setObjectName("lineEdit_PD_UserName")
        self.lineEdit_PD_Changes = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_PD_Changes.setGeometry(QtCore.QRect(190, 100, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_PD_Changes.setFont(font)
        self.lineEdit_PD_Changes.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_PD_Changes.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PD_Changes.setObjectName("lineEdit_PD_Changes")
        self.label_PerforceDescription = QtWidgets.QLabel(self.frame)
        self.label_PerforceDescription.setGeometry(QtCore.QRect(30, 0, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_PerforceDescription.setFont(font)
        self.label_PerforceDescription.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PerforceDescription.setObjectName("label_PerforceDescription")
        self.pushButton_ClearPerforceDescription = QtWidgets.QPushButton(self.frame)
        self.pushButton_ClearPerforceDescription.setGeometry(QtCore.QRect(470, 10, 23, 23))
        self.pushButton_ClearPerforceDescription.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_ClearPerforceDescription.setObjectName("pushButton_ClearPerforceDescription")
        self.PerforceIcon = QtWidgets.QPushButton(self.frame)
        self.PerforceIcon.setEnabled(False)
        self.PerforceIcon.setGeometry(QtCore.QRect(0, 2, 30, 30))
        font = QtGui.QFont()
        font.setKerning(False)
        self.PerforceIcon.setFont(font)
        self.PerforceIcon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("icon1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PerforceIcon.setIcon(icon1)
        self.PerforceIcon.setIconSize(QtCore.QSize(25, 25))
        self.PerforceIcon.setFlat(True)
        self.PerforceIcon.setObjectName("PerforceIcon")
        self.label_PD_ProjectName.raise_()
        self.label_PD_UserName.raise_()
        self.label_PD_Changes.raise_()
        self.lineEdit_PD_ProjectName.raise_()
        self.lineEdit_PD_UserName.raise_()
        self.lineEdit_PD_Changes.raise_()
        self.pushButton_ClearPerforceDescription.raise_()
        self.PerforceIcon.raise_()
        self.label_PerforceDescription.raise_()
        self.pushButton_PerforceDescription.raise_()
        self.verticalLayout.addWidget(self.frame)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.pushButton_PersistChanges = QtWidgets.QPushButton(self.widget)
        self.pushButton_PersistChanges.setGeometry(QtCore.QRect(190, 20, 75, 23))
        self.pushButton_PersistChanges.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_PersistChanges.setObjectName("pushButton_PersistChanges")
        self.lineEdit_PC_ChangelistNumber = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_PC_ChangelistNumber.setGeometry(QtCore.QRect(190, 80, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_PC_ChangelistNumber.setFont(font)
        self.lineEdit_PC_ChangelistNumber.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_PC_ChangelistNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PC_ChangelistNumber.setObjectName("lineEdit_PC_ChangelistNumber")
        self.label_PC_ChangelistNumber = QtWidgets.QLabel(self.widget)
        self.label_PC_ChangelistNumber.setGeometry(QtCore.QRect(0, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PC_ChangelistNumber.setFont(font)
        self.label_PC_ChangelistNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PC_ChangelistNumber.setObjectName("label_PC_ChangelistNumber")
        self.label_PC_LevelName = QtWidgets.QLabel(self.widget)
        self.label_PC_LevelName.setGeometry(QtCore.QRect(0, 50, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PC_LevelName.setFont(font)
        self.label_PC_LevelName.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PC_LevelName.setObjectName("label_PC_LevelName")
        self.label_PersistChanges = QtWidgets.QLabel(self.widget)
        self.label_PersistChanges.setGeometry(QtCore.QRect(30, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_PersistChanges.setFont(font)
        self.label_PersistChanges.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PersistChanges.setObjectName("label_PersistChanges")
        self.lineEdit_PC_LevelName = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_PC_LevelName.setGeometry(QtCore.QRect(190, 50, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_PC_LevelName.setFont(font)
        self.lineEdit_PC_LevelName.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_PC_LevelName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PC_LevelName.setObjectName("lineEdit_PC_LevelName")
        self.pushButton_ClearPersistChange = QtWidgets.QPushButton(self.widget)
        self.pushButton_ClearPersistChange.setGeometry(QtCore.QRect(470, 20, 23, 23))
        self.pushButton_ClearPersistChange.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_ClearPersistChange.setObjectName("pushButton_ClearPersistChange")
        self.PerforceIcon_2 = QtWidgets.QPushButton(self.widget)
        self.PerforceIcon_2.setEnabled(False)
        self.PerforceIcon_2.setGeometry(QtCore.QRect(0, 12, 30, 30))
        font = QtGui.QFont()
        font.setKerning(False)
        self.PerforceIcon_2.setFont(font)
        self.PerforceIcon_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("icon4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PerforceIcon_2.setIcon(icon2)
        self.PerforceIcon_2.setIconSize(QtCore.QSize(25, 25))
        self.PerforceIcon_2.setFlat(True)
        self.PerforceIcon_2.setObjectName("PerforceIcon_2")
        self.lineEdit_PC_ChangelistNumber.raise_()
        self.label_PC_ChangelistNumber.raise_()
        self.label_PC_LevelName.raise_()
        self.label_PersistChanges.raise_()
        self.lineEdit_PC_LevelName.raise_()
        self.pushButton_ClearPersistChange.raise_()
        self.PerforceIcon_2.raise_()
        self.pushButton_PersistChanges.raise_()
        self.verticalLayout.addWidget(self.widget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit_SS_UnrealNote = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_SS_UnrealNote.setGeometry(QtCore.QRect(190, 130, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_SS_UnrealNote.setFont(font)
        self.textEdit_SS_UnrealNote.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "")
        self.textEdit_SS_UnrealNote.setObjectName("textEdit_SS_UnrealNote")
        self.label_SS_ShotCode = QtWidgets.QLabel(self.frame_2)
        self.label_SS_ShotCode.setGeometry(QtCore.QRect(0, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SS_ShotCode.setFont(font)
        self.label_SS_ShotCode.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_SS_ShotCode.setObjectName("label_SS_ShotCode")
        self.label_SS_UnrealNote = QtWidgets.QLabel(self.frame_2)
        self.label_SS_UnrealNote.setGeometry(QtCore.QRect(0, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SS_UnrealNote.setFont(font)
        self.label_SS_UnrealNote.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_SS_UnrealNote.setObjectName("label_SS_UnrealNote")
        self.label_Snapshot = QtWidgets.QLabel(self.frame_2)
        self.label_Snapshot.setGeometry(QtCore.QRect(30, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Snapshot.setFont(font)
        self.label_Snapshot.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Snapshot.setObjectName("label_Snapshot")
        self.lineEdit_SS_SequenceName = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_SS_SequenceName.setGeometry(QtCore.QRect(190, 70, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_SS_SequenceName.setFont(font)
        self.lineEdit_SS_SequenceName.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_SS_SequenceName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_SS_SequenceName.setObjectName("lineEdit_SS_SequenceName")
        self.lineEdit_SS_LevelName = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_SS_LevelName.setGeometry(QtCore.QRect(190, 100, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_SS_LevelName.setFont(font)
        self.lineEdit_SS_LevelName.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_SS_LevelName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_SS_LevelName.setObjectName("lineEdit_SS_LevelName")
        self.label_SS_SequenceName = QtWidgets.QLabel(self.frame_2)
        self.label_SS_SequenceName.setGeometry(QtCore.QRect(0, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SS_SequenceName.setFont(font)
        self.label_SS_SequenceName.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_SS_SequenceName.setObjectName("label_SS_SequenceName")
        self.pushButton_Snapshot = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Snapshot.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.pushButton_Snapshot.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_Snapshot.setObjectName("pushButton_Snapshot")
        self.lineEdit_SS_ShotCode = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_SS_ShotCode.setGeometry(QtCore.QRect(190, 40, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_SS_ShotCode.setFont(font)
        self.lineEdit_SS_ShotCode.setStyleSheet("background: rgb(25, 25, 25);\n"
        "color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(0, 0, 255);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.lineEdit_SS_ShotCode.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_SS_ShotCode.setObjectName("lineEdit_SS_ShotCode")
        self.label_SS_LevelName = QtWidgets.QLabel(self.frame_2)
        self.label_SS_LevelName.setGeometry(QtCore.QRect(0, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SS_LevelName.setFont(font)
        self.label_SS_LevelName.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_SS_LevelName.setObjectName("label_SS_LevelName")
        self.pushButton_ClearSpanshot = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_ClearSpanshot.setGeometry(QtCore.QRect(470, 10, 23, 23))
        self.pushButton_ClearSpanshot.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);")
        self.pushButton_ClearSpanshot.setObjectName("pushButton_ClearSpanshot")
        self.PerforceIcon_3 = QtWidgets.QPushButton(self.frame_2)
        self.PerforceIcon_3.setEnabled(False)
        self.PerforceIcon_3.setGeometry(QtCore.QRect(0, 2, 30, 30))
        font = QtGui.QFont()
        font.setKerning(False)
        self.PerforceIcon_3.setFont(font)
        self.PerforceIcon_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("icon3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PerforceIcon_3.setIcon(icon3)
        self.PerforceIcon_3.setIconSize(QtCore.QSize(25, 25))
        self.PerforceIcon_3.setAutoDefault(False)
        self.PerforceIcon_3.setDefault(False)
        self.PerforceIcon_3.setFlat(True)
        self.PerforceIcon_3.setObjectName("PerforceIcon_3")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        ####  Connect the push buttons
        self.pushButton_ClearLabelOutput.clicked.connect(self.ClearLabelOutput) 
        self.pushButton_ReadNote.clicked.connect(self.ReadNote)
        self.pushButton_SaveNote.clicked.connect(self.SaveNote) 
        self.pushButton_PerforceDescription.clicked.connect(self.OnPressedBtPerforceDescription) 
        self.pushButton_ClearPerforceDescription.clicked.connect(self.ClearPerforceDescription)
        self.pushButton_PersistChanges.clicked.connect(self.OnPressedBtPersistChanges) 
        self.pushButton_ClearPersistChange.clicked.connect(self.ClearPersistChange)
        self.pushButton_Snapshot.clicked.connect(self.OnPressedBtSnapshot) 
        self.pushButton_ClearSpanshot.clicked.connect(self.ClearSnapshot) 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beacon Supporter"))
        self.pushButton_ClearLabelOutput.setText(_translate("MainWindow", "X"))
        self.label_Output.setText(_translate("MainWindow", "Send the data"))
        self.label_TempText_2.setText(_translate("MainWindow", "Note.txt"))
        self.pushButton_SaveNote.setText(_translate("MainWindow", "Save"))
        self.pushButton_ReadNote.setText(_translate("MainWindow", "Read"))
        self.pushButton_PerforceDescription.setText(_translate("MainWindow", "Generate"))
        self.label_PD_ProjectName.setText(_translate("MainWindow", "Project Name"))
        self.label_PD_UserName.setText(_translate("MainWindow", "User Name"))
        self.label_PD_Changes.setText(_translate("MainWindow", "Changes"))
        self.label_PerforceDescription.setText(_translate("MainWindow", "Perforce"))
        self.pushButton_ClearPerforceDescription.setText(_translate("MainWindow", "X"))
        self.pushButton_PersistChanges.setText(_translate("MainWindow", "Generate"))
        self.label_PC_ChangelistNumber.setText(_translate("MainWindow", "P4V Changelist Number"))
        self.label_PC_LevelName.setText(_translate("MainWindow", "Level Name"))
        self.label_PersistChanges.setText(_translate("MainWindow", "Changelist"))
        self.pushButton_ClearPersistChange.setText(_translate("MainWindow", "X"))
        self.label_SS_ShotCode.setText(_translate("MainWindow", "Shot Code"))
        self.label_SS_UnrealNote.setText(_translate("MainWindow", "Unreal Note"))
        self.label_Snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.label_SS_SequenceName.setText(_translate("MainWindow", "Sequence Name"))
        self.pushButton_Snapshot.setText(_translate("MainWindow", "Generate"))
        self.label_SS_LevelName.setText(_translate("MainWindow", "Level Name"))
        self.pushButton_ClearSpanshot.setText(_translate("MainWindow", "X"))


#### define the button trigger functions
    def OnPressedBtPerforceDescription(self):
        UserName = self.lineEdit_PD_UserName.text()
        ProjectName = self.lineEdit_PD_ProjectName.text()
        UEChanges = self.lineEdit_PD_Changes.text()
        ExpPerforceDescription = UserName + " - " + ProjectName + " - " + UEChanges
        
        CurrentOutput = self.label_Output.text()
        if (CurrentOutput == "Send the data" or CurrentOutput == ""):
            self.label_Output.setText(ExpPerforceDescription)#### when button was pressed, collect all the data from Perforce Description
        else:
            self.label_Output.setText(CurrentOutput + "\n" + "\n" +ExpPerforceDescription)

    def OnPressedBtPersistChanges(self):
        LevelName = self.lineEdit_PC_LevelName.text()
        ChangeListNum = self.lineEdit_PC_ChangelistNumber.text()
        PersistChange = "Level Name : " + LevelName + "\n" + "P4V Changelist Number : " + ChangeListNum
        CurrentOutput = self.label_Output.text()
        if(CurrentOutput == "Send the data" or CurrentOutput == ""):
            self.label_Output.setText(PersistChange)
        else:
            self.label_Output.setText(CurrentOutput + "\n" + "\n" + PersistChange)


    def OnPressedBtSnapshot(self):
        Shotcode = self.lineEdit_SS_ShotCode.text()
        SequenceName = self.lineEdit_SS_SequenceName.text()
        LevelName = self.lineEdit_SS_LevelName.text()
        UnrealNote = "\n" + self.textEdit_SS_UnrealNote.toPlainText()
        CurrentOutput = self.label_Output.text()
        Snapshot = Shotcode + "\n" + "Sequence Name : " + SequenceName + "\n" + "Level Name : " + LevelName + "\n" + "Unreal Note : " + UnrealNote
        if(CurrentOutput == "Send the data" or CurrentOutput == ""):
            self.label_Output.setText(Snapshot)
        else:
            self.label_Output.setText(CurrentOutput + "\n" + "\n" + Snapshot)
        print(Shotcode)

    def ClearPerforceDescription(self):
        self.lineEdit_PD_ProjectName.setText("")
        self.lineEdit_PD_UserName.setText("")
        self.lineEdit_PD_Changes.setText("")


    def ClearPersistChange(self):
        self.lineEdit_PC_LevelName.setText("")
        self.lineEdit_PC_ChangelistNumber.setText("")

    def ClearSnapshot(self):
        self.lineEdit_SS_ShotCode.setText("")
        self.lineEdit_SS_LevelName.setText("")
        self.lineEdit_SS_SequenceName.setText("")
        self.textEdit_SS_UnrealNote.setText("")

    def ClearLabelOutput(self):
        self.label_Output.setText("")

    def SaveNote(self):
        Content = self.textEdit_SS_TempNote.toPlainText()
        file_filter = "Text File(*.txt)"
        fname = QtWidgets.QFileDialog.getSaveFileName(filter=file_filter)
        fileName = fname[0]
        file = open(fileName, "w")
        file.write(Content)
        file.close()

    def ReadNote(self):
        file_filter = "Text File(*.txt)"
        fname = QtWidgets.QFileDialog.getOpenFileName(filter=file_filter)
        fileName = fname[0]
        file = open(fileName, "r")
        Content = file.readlines()
        PureString = "".join(Content)
        self.textEdit_SS_TempNote.setPlainText(PureString)


#### pack the image
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
