"""

******** OBS: ARQUIVO PRINCIPAL ALTERADO PARA "downloader.py". ***********

from pytube import YouTube
from pytube.exceptions import *
import os

def mostrar_progresso(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    print(f"Progresso: {progress:.2f}%")



try:
    link = str(input('Digite o link do youtube: '))
    yt = YouTube(link, on_progress_callback=mostrar_progresso)
    titulo_do_video = yt.title
    escolha_usuario = str(input('O que você quer baixar?\n'
                                '[1] - Apenas áudio (MP3)\n'
                                '[2] - Video com áudio (MP4)\n'
                                'Sua escolha: '))
    print('Obs: o arquivo será baixado no diretório atual.')

    if escolha_usuario == '1':
        try:
            video = yt.streams.get_audio_only()
            print(f'Baixando áudio: {titulo_do_video}...')
            print(f'Qualidade: ', video.abr)
            arquivo_em_video = video.download()
            base, extensao = os.path.splitext(arquivo_em_video)
            arquivo_em_audio = base + '.mp3'
            os.rename(arquivo_em_video, arquivo_em_audio)
        except FileExistsError:
            print('O arquivo já existe no diretório, portanto não foi baixado.')
        except:
            print('Ocorreu algum erro.')
        else:
            print('Arquivo baixado com êxito.')

        # Também poderia ser feito dessa forma, com o replace, desde que o arquivo fosse sempre em .mp4
        # arquivo_em_audio = arquivo_em_video.replace('.mp4', '.mp3')
        # os.rename(arquivo_em_video, arquivo_em_audio)

    elif escolha_usuario == '2':
        try:
            stream = yt.streams.get_highest_resolution()
            print(f'Baixando vídeo: {titulo_do_video}...')
            print(f'Qualidade: {stream.resolution} | {stream.fps}fps')
            stream.download()
        except FileExistsError:
            print('O arquivo já existe no diretório, portanto não foi baixado.')
        except:
            print('Ocorreu algum erro.')
        else:
            print('Arquivo baixado com êxito.')
    else:
        print('Opção inválida. Execute o programa novamente para baixar áudio ou video do youtube.')
except VideoUnavailable:
    print(f'O vídeo não está disponível.')
except:
    print('Ops, talvez o link esteja quebrado ou incorreto. Verifique, por favor!')
"""