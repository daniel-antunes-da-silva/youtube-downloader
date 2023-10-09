from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)
import QtDesigner.resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(570, 292)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/download_ytb.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.txtUrl = QLineEdit(Widget)
        self.txtUrl.setObjectName(u"txtUrl")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(97)
        sizePolicy1.setHeightForWidth(self.txtUrl.sizePolicy().hasHeightForWidth())
        self.txtUrl.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.txtUrl)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(200, -1, -1, -1)
        self.radioBtnMp3 = QRadioButton(Widget)
        self.radioBtnMp3.setObjectName(u"radioBtnMp3")
        self.radioBtnMp3.setFont(font)

        self.horizontalLayout_2.addWidget(self.radioBtnMp3)

        self.radioBtnMp4 = QRadioButton(Widget)
        self.radioBtnMp4.setObjectName(u"radioBtnMp4")
        self.radioBtnMp4.setFont(font)

        self.horizontalLayout_2.addWidget(self.radioBtnMp4)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 30)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.barraProgresso = QProgressBar(Widget)
        self.barraProgresso.setObjectName(u"barraProgresso")
        self.barraProgresso.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.barraProgresso.sizePolicy().hasHeightForWidth())
        self.barraProgresso.setSizePolicy(sizePolicy2)
        self.barraProgresso.setMaximumSize(QSize(989435, 30))
        self.barraProgresso.setLayoutDirection(Qt.LeftToRight)
        self.barraProgresso.setAutoFillBackground(False)
        self.barraProgresso.setValue(21)
        self.barraProgresso.setAlignment(Qt.AlignCenter)
        self.barraProgresso.setTextVisible(False)
        self.barraProgresso.setOrientation(Qt.Horizontal)
        self.barraProgresso.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.barraProgresso)

        self.btnDownload = QPushButton(Widget)
        self.btnDownload.setObjectName(u"btnDownload")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.btnDownload.setFont(font1)

        self.verticalLayout.addWidget(self.btnDownload)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Youtube Downloader", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Link do v\u00eddeo:", None))
        self.radioBtnMp3.setText(QCoreApplication.translate("Widget", u"MP3", None))
        self.radioBtnMp4.setText(QCoreApplication.translate("Widget", u"MP4", None))
        self.btnDownload.setText(QCoreApplication.translate("Widget", u"Download", None))
    # retranslateUi

