from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)
import QtDesigner.resource_rc


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(511, 385)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/download_ytb.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        self.btnDownload = QPushButton(Widget)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setGeometry(QRect(320, 130, 131, 29))
        self.btnDownload.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.btnDownload.setFont(font)
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(126, 90, 321, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(200, 0, 0, 0)
        self.radioBtnMp3 = QRadioButton(self.layoutWidget)
        self.radioBtnMp3.setObjectName(u"radioBtnMp3")
        font1 = QFont()
        font1.setPointSize(12)
        self.radioBtnMp3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioBtnMp3)

        self.radioBtnMp4 = QRadioButton(self.layoutWidget)
        self.radioBtnMp4.setObjectName(u"radioBtnMp4")
        self.radioBtnMp4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioBtnMp4)

        self.horizontalLayout_2.setStretch(1, 30)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 96, 21))
        self.label.setFont(font1)
        self.txtUrl = QLineEdit(Widget)
        self.txtUrl.setObjectName(u"txtUrl")
        self.txtUrl.setGeometry(QRect(150, 50, 301, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(97)
        sizePolicy1.setHeightForWidth(self.txtUrl.sizePolicy().hasHeightForWidth())
        self.txtUrl.setSizePolicy(sizePolicy1)
        self.txtInformativo = QTextEdit(Widget)
        self.txtInformativo.setObjectName(u"txtInformativo")
        self.txtInformativo.setEnabled(True)
        self.txtInformativo.setGeometry(QRect(40, 210, 411, 141))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(40, 190, 71, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Youtube Downloader", None))
        self.btnDownload.setText(QCoreApplication.translate("Widget", u"Download", None))
        self.radioBtnMp3.setText(QCoreApplication.translate("Widget", u"MP3", None))
        self.radioBtnMp4.setText(QCoreApplication.translate("Widget", u"MP4", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Link do v\u00eddeo:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Informativo:", None))
    # retranslateUi

