# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'concate_page.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidgetItem, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, Pivot,
    PrimaryPushButton, ProgressBar, PushButton, RadioButton,
    SegmentedWidget, SimpleCardWidget, StrongBodyLabel, VerticalSeparator)
from src.components.draggable_list_widget import DraggableListWidget
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1100, 650)
        Form.setStyleSheet(u"background-color: rgba(0, 0, 0);")
        self.verticalLayout_7 = QVBoxLayout(Form)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SimpleCardWidget = SimpleCardWidget(Form)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.SimpleCardWidget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.StrongBodyLabel = StrongBodyLabel(self.SimpleCardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StrongBodyLabel.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel.setSizePolicy(sizePolicy)
        self.StrongBodyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.StrongBodyLabel)

        self.listWidget = DraggableListWidget(self.SimpleCardWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.Box)
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setDragEnabled(True)

        self.verticalLayout_5.addWidget(self.listWidget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.PushButton = PushButton(self.SimpleCardWidget)
        self.PushButton.setObjectName(u"PushButton")
        icon = QIcon()
        icon.addFile(u":/images/images/add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.PushButton.setIcon(icon)
        self.PushButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.PushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_12 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_12.setObjectName(u"BodyLabel_12")

        self.horizontalLayout.addWidget(self.BodyLabel_12)

        self.RadioButton_2 = RadioButton(self.SimpleCardWidget)
        self.RadioButton_2.setObjectName(u"RadioButton_2")
        self.RadioButton_2.setChecked(True)

        self.horizontalLayout.addWidget(self.RadioButton_2)

        self.RadioButton = RadioButton(self.SimpleCardWidget)
        self.RadioButton.setObjectName(u"RadioButton")

        self.horizontalLayout.addWidget(self.RadioButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.BodyLabel)

        self.ComboBox_2 = ComboBox(self.SimpleCardWidget)
        self.ComboBox_2.setObjectName(u"ComboBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ComboBox_2.sizePolicy().hasHeightForWidth())
        self.ComboBox_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.ComboBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.horizontalLayout_7.addWidget(self.SimpleCardWidget)

        self.SimpleCardWidget_2 = SimpleCardWidget(Form)
        self.SimpleCardWidget_2.setObjectName(u"SimpleCardWidget_2")
        self.SimpleCardWidget_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.SimpleCardWidget_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SegmentedWidget = SegmentedWidget(self.SimpleCardWidget_2)
        self.SegmentedWidget.setObjectName(u"SegmentedWidget")

        self.verticalLayout_4.addWidget(self.SegmentedWidget)

        self.stackedWidget = QStackedWidget(self.SimpleCardWidget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.PushButton_2 = PushButton(self.page)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.horizontalLayout_5.addWidget(self.PushButton_2)

        self.PushButton_3 = PushButton(self.page)
        self.PushButton_3.setObjectName(u"PushButton_3")

        self.horizontalLayout_5.addWidget(self.PushButton_3)

        self.PushButton_4 = PushButton(self.page)
        self.PushButton_4.setObjectName(u"PushButton_4")

        self.horizontalLayout_5.addWidget(self.PushButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout_7.addWidget(self.SimpleCardWidget_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        self.verticalLayout_6 = QVBoxLayout(self.CardWidget)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel_2 = BodyLabel(self.CardWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.horizontalLayout_3.addWidget(self.BodyLabel_2)

        self.ProgressBar_2 = ProgressBar(self.CardWidget)
        self.ProgressBar_2.setObjectName(u"ProgressBar_2")
        sizePolicy2.setHeightForWidth(self.ProgressBar_2.sizePolicy().hasHeightForWidth())
        self.ProgressBar_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.ProgressBar_2)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.BodyLabel_4 = BodyLabel(self.CardWidget)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        sizePolicy1.setHeightForWidth(self.BodyLabel_4.sizePolicy().hasHeightForWidth())
        self.BodyLabel_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.BodyLabel_4)

        self.BodyLabel_10 = BodyLabel(self.CardWidget)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")
        sizePolicy1.setHeightForWidth(self.BodyLabel_10.sizePolicy().hasHeightForWidth())
        self.BodyLabel_10.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.BodyLabel_10)

        self.BodyLabel_6 = BodyLabel(self.CardWidget)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")
        sizePolicy1.setHeightForWidth(self.BodyLabel_6.sizePolicy().hasHeightForWidth())
        self.BodyLabel_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.BodyLabel_6)

        self.VerticalSeparator = VerticalSeparator(self.CardWidget)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout_3.addWidget(self.VerticalSeparator)

        self.BodyLabel_8 = BodyLabel(self.CardWidget)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")
        sizePolicy1.setHeightForWidth(self.BodyLabel_8.sizePolicy().hasHeightForWidth())
        self.BodyLabel_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.BodyLabel_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_3 = BodyLabel(self.CardWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.horizontalLayout_4.addWidget(self.BodyLabel_3)

        self.ProgressBar = ProgressBar(self.CardWidget)
        self.ProgressBar.setObjectName(u"ProgressBar")

        self.horizontalLayout_4.addWidget(self.ProgressBar)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.BodyLabel_5 = BodyLabel(self.CardWidget)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")
        sizePolicy1.setHeightForWidth(self.BodyLabel_5.sizePolicy().hasHeightForWidth())
        self.BodyLabel_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.BodyLabel_5)

        self.BodyLabel_11 = BodyLabel(self.CardWidget)
        self.BodyLabel_11.setObjectName(u"BodyLabel_11")
        sizePolicy1.setHeightForWidth(self.BodyLabel_11.sizePolicy().hasHeightForWidth())
        self.BodyLabel_11.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.BodyLabel_11)

        self.BodyLabel_7 = BodyLabel(self.CardWidget)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")
        sizePolicy1.setHeightForWidth(self.BodyLabel_7.sizePolicy().hasHeightForWidth())
        self.BodyLabel_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.BodyLabel_7)

        self.VerticalSeparator_2 = VerticalSeparator(self.CardWidget)
        self.VerticalSeparator_2.setObjectName(u"VerticalSeparator_2")

        self.horizontalLayout_4.addWidget(self.VerticalSeparator_2)

        self.BodyLabel_9 = BodyLabel(self.CardWidget)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")
        sizePolicy1.setHeightForWidth(self.BodyLabel_9.sizePolicy().hasHeightForWidth())
        self.BodyLabel_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.BodyLabel_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/start_merge.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.PrimaryPushButton.setIcon(icon1)
        self.PrimaryPushButton.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.PrimaryPushButton)


        self.verticalLayout_7.addWidget(self.CardWidget)

#if QT_CONFIG(shortcut)
        self.StrongBodyLabel.setBuddy(self.listWidget)
        self.BodyLabel_12.setBuddy(self.RadioButton_2)
        self.BodyLabel.setBuddy(self.ComboBox_2)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.listWidget, self.PushButton)
        QWidget.setTabOrder(self.PushButton, self.RadioButton_2)
        QWidget.setTabOrder(self.RadioButton_2, self.RadioButton)
        QWidget.setTabOrder(self.RadioButton, self.ComboBox_2)
        QWidget.setTabOrder(self.ComboBox_2, self.PushButton_2)
        QWidget.setTabOrder(self.PushButton_2, self.PushButton_3)
        QWidget.setTabOrder(self.PushButton_3, self.PushButton_4)
        QWidget.setTabOrder(self.PushButton_4, self.PrimaryPushButton)

        self.retranslateUi(Form)
        self.ProgressBar_2.valueChanged.connect(self.BodyLabel_4.setNum)
        self.ProgressBar.valueChanged.connect(self.BodyLabel_5.setNum)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.StrongBodyLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5c06\u89c6\u9891\u62d6\u653e\u5230\u4e0b\u65b9\u5217\u8868\u4e2d,\u53f3\u952e\u6709\u66f4\u591a\u9009\u9879</p><p>(Tip: \u53ef\u4ee5\u901a\u8fc7\u62d6\u653e\u4e00\u4e2a\u6bcf\u4e00\u884c\u4e00\u4e2a\u89c6\u9891\u8def\u5f84\u7684txt\u653e\u7f6e\u5927\u91cf\u89c6\u9891\u6587\u4ef6,\u6b64\u65b9\u5f0f\u6bd4\u76f4\u63a5\u62d6\u52a8\u89c6\u9891\u66f4\u5feb)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u6587\u4ef6\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("Form", u"\u5c06\u89c6\u9891\u62d6\u653e\u5230\u4e0b\u65b9\u5217\u8868\u4e2d,\u53f3\u952e\u6709\u66f4\u591a\u9009\u9879\n"
"(Tip: \u53ef\u4ee5\u901a\u8fc7\u62d6\u653e\u4e00\u4e2a\u6bcf\u4e00\u884c\u4e00\u4e2a\u89c6\u9891\u8def\u5f84\u7684txt\u653e\u7f6e\u5927\u91cf\u89c6\u9891\u6587\u4ef6,\u6b64\u65b9\u5f0f\u6bd4\u76f4\u63a5\u62d6\u52a8\u89c6\u9891\u66f4\u5feb)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.PushButton.setToolTip(QCoreApplication.translate("Form", u"\u9009\u62e9\u9700\u8981\u88ab\u5408\u6210\u7684\u89c6\u9891", None))
#endif // QT_CONFIG(tooltip)
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u89c6\u9891", None))
#if QT_CONFIG(tooltip)
        self.BodyLabel_12.setToolTip(QCoreApplication.translate("Form", u"\u60a8\u6700\u7ec8\u5e0c\u671b\u5bfc\u51fa\u7684\u89c6\u9891\u662f\u6a2a\u5c4f\u89c6\u9891\u8fd8\u662f\u7ad6\u5c4f\u89c6\u9891", None))
#endif // QT_CONFIG(tooltip)
        self.BodyLabel_12.setText(QCoreApplication.translate("Form", u"\u60a8\u5e0c\u671b\u5c06\u89c6\u9891\u8f93\u51fa\u4e3a", None))
#if QT_CONFIG(tooltip)
        self.RadioButton_2.setToolTip(QCoreApplication.translate("Form", u"\u60a8\u6700\u7ec8\u5e0c\u671b\u5bfc\u51fa\u7684\u89c6\u9891\u662f\u6a2a\u5c4f\u89c6\u9891\u8fd8\u662f\u7ad6\u5c4f\u89c6\u9891", None))
#endif // QT_CONFIG(tooltip)
        self.RadioButton_2.setText(QCoreApplication.translate("Form", u"\u7ad6\u5c4f\u89c6\u9891", None))
#if QT_CONFIG(tooltip)
        self.RadioButton.setToolTip(QCoreApplication.translate("Form", u"\u60a8\u6700\u7ec8\u5e0c\u671b\u5bfc\u51fa\u7684\u89c6\u9891\u662f\u6a2a\u5c4f\u89c6\u9891\u8fd8\u662f\u7ad6\u5c4f\u89c6\u9891", None))
#endif // QT_CONFIG(tooltip)
        self.RadioButton.setText(QCoreApplication.translate("Form", u"\u6a2a\u5c4f\u89c6\u9891", None))
#if QT_CONFIG(tooltip)
        self.BodyLabel.setToolTip(QCoreApplication.translate("Form", u"\u5982\u679c\u60a8\u7684\u89c6\u9891\u7ecf\u8fc7\u68c0\u6d4b\u4e4b\u540e\u53d1\u73b0\u4e0d\u7b26\u5408\u4f60\u4e0a\u9762\u7684\u9009\u9879\u4f60\u8981\u5982\u4f55\u5904\u7406?", None))
#endif // QT_CONFIG(tooltip)
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u4e0d\u7b26\u5408\u671d\u5411\u5982\u4f55\u8c03\u6574", None))
#if QT_CONFIG(tooltip)
        self.ComboBox_2.setToolTip(QCoreApplication.translate("Form", u"\u5982\u679c\u60a8\u7684\u89c6\u9891\u7ecf\u8fc7\u68c0\u6d4b\u4e4b\u540e\u53d1\u73b0\u4e0d\u7b26\u5408\u4f60\u4e0a\u9762\u7684\u9009\u9879\u4f60\u8981\u5982\u4f55\u5904\u7406?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.SegmentedWidget.setToolTip(QCoreApplication.translate("Form", u"\u9009\u62e9\u4e0d\u540c\u7684\u9884\u89c8\u65b9\u5f0f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u5728\u8bbe\u7f6e\u9875\u9762\u8bbe\u7f6e\u9ed8\u8ba4\u5c55\u793a\u54ea\u4e00\u4e2a\u753b\u9762(\u9ed8\u8ba4\u4e3a\u4e0d\u4e3a\u9ed1\u8272\u7684\u7b2c\u4e00\u5e27)", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u663e\u793a\u56fe\u7247", None))
#if QT_CONFIG(tooltip)
        self.PushButton_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u987a\u65f6\u9488\u65cb\u8f6c90\u00b0", None))
        self.PushButton_3.setText(QCoreApplication.translate("Form", u"\u9006\u65f6\u9488\u65cb\u8f6c90\u00b0", None))
        self.PushButton_4.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e0b\u98a0\u5012", None))
#if QT_CONFIG(tooltip)
        self.BodyLabel_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u603b\u8fdb\u5ea6", None))
        self.ProgressBar_2.setFormat(QCoreApplication.translate("Form", u"(%v/%m) %p%", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8fdb\u5ea6", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Form", u"/", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u603b\u8fdb\u5ea6", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Form", u"\u767e\u5206\u6bd4", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u8be6\u7ec6\u8fdb\u5ea6", None))
        self.ProgressBar.setFormat(QCoreApplication.translate("Form", u"(%v/%m) %p%", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8fdb\u5ea6", None))
        self.BodyLabel_11.setText(QCoreApplication.translate("Form", u"/", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u603b\u8fdb\u5ea6", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("Form", u"\u767e\u5206\u6bd4", None))
#if QT_CONFIG(tooltip)
        self.PrimaryPushButton.setToolTip(QCoreApplication.translate("Form", u"\u70b9\u51fb\u6b64\u5904\u76f4\u63a5\u5f00\u59cb\u5408\u5e76\uff0c\u60a8\u53ef\u4ee5\u901a\u8fc7\u5728\u8bbe\u7f6e\u9875\u9762\u5b9a\u4e49\u8f93\u51fa\u6587\u4ef6\u4f4d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5408\u5e76", None))
    # retranslateUi
