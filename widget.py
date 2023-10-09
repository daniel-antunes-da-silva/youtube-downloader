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
        self.barraProgresso.setValue(0)
        self.barraProgresso.setVisible(False)
        self.btnDownload.clicked.connect(self.download)

    def mostrar_progresso(self, stream, chunk, bytes_remaining):
        self.barraProgresso.setVisible(True)
        self.barraProgresso.setTextVisible(True)
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress = (bytes_downloaded / total_size) * 100
        self.barraProgresso.setValue(progress)

    def download(self):
        if self.radioBtnMp3.isChecked():
            formato = '.mp3'
        elif self.radioBtnMp4.isChecked():
            formato = '.mp4'
        else:
            QMessageBox.information(self, 'Info',
                                     f'Formato não selecionado',
                                     QMessageBox.Ok | QMessageBox.Cancel)

        try:
            link = self.txtUrl.text()
            yt = YouTube(link, on_progress_callback=self.mostrar_progresso)
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

        except:
            QMessageBox.warning(self, 'Atenção!',
                                'Ocorreu algum erro!',
                                QMessageBox.Ok | QMessageBox.Cancel)

        else:
            if formato == '.mp3':
                qualidade = video.abr
            else:
                qualidade = f'{stream.resolution} | {stream.fps}'
            QMessageBox.information(self, 'Info',
                                    f'Arquivo baixado com êxito!\n'
                                    f'Qualidade: {qualidade}',
                                    QMessageBox.Ok | QMessageBox.Cancel)