import sys
from time import sleep

from PySide6.QtWidgets import QWidget, QMessageBox
from QtDesigner.ui_widget import Ui_Widget
from pytube import YouTube
import os
from pytube.exceptions import VideoUnavailable
from threading import Thread


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnDownload.clicked.connect(self.download)
        self.label_2.setVisible(False)
        self.txtInformativo.setVisible(False)
        sys.stdout = self
        self.original_stdout = sys.__stdout__

    def write(self, texto):
        self.txtInformativo.insertPlainText(texto)

    def download(self):
        self.label_2.setVisible(True)
        self.txtInformativo.setVisible(True)
        try:
            if self.radioBtnMp3.isChecked():
                formato = '.mp3'
            elif self.radioBtnMp4.isChecked():
                formato = '.mp4'
            else:
                QMessageBox.information(self, 'Info',
                                         f'Formato não selecionado',
                                         QMessageBox.Ok | QMessageBox.Cancel)
                return

            link = self.txtUrl.text()
            yt = YouTube(link)
            titulo_do_video = yt.title

            if formato == '.mp3':
                video = yt.streams.get_audio_only()
                print(f'Baixando áudio: {titulo_do_video}...')
                print(f'Qualidade: ', video.abr)
                arquivo_em_video = video.download()
                base, extensao = os.path.splitext(arquivo_em_video)
                arquivo_em_audio = base + f'{formato}'
                os.rename(arquivo_em_video, arquivo_em_audio)
            elif formato == '.mp4':
                stream = yt.streams.get_highest_resolution()
                print(f'Baixando vídeo: {titulo_do_video}...')
                print(f'Qualidade: {stream.resolution} | {stream.fps}fps')
                stream.download()

        except FileExistsError:
            print('O arquivo já existe no diretório, portanto não foi baixado.')

        except VideoUnavailable:
            QMessageBox.critical(self, 'Aviso',
                                 'O vídeo que você está tentando baixar não está disponível!',
                                 QMessageBox.Ok | QMessageBox.Cancel)

        except Exception as erro:
            QMessageBox.warning(self, 'Erro!',
                                f'{erro}!',
                                QMessageBox.Ok | QMessageBox.Cancel)

        else:
            if formato == '.mp3':
                qualidade = video.abr
            else:
                qualidade = f'{stream.resolution} | {stream.fps}'
            QMessageBox.information(self, 'Mensagem de informação',
                                    f'Arquivo baixado com êxito!\nQualidade: {qualidade}',
                                    QMessageBox.Ok | QMessageBox.Cancel)
