from pytube import YouTube
import os

link = str(input('Digite o link do youtube: '))
yt = YouTube(link)
titulo_do_video = yt.title
escolha_usuario = str(input('O que você quer baixar?\n'
                            '[1] - MP3\n'
                            '[2] - MP4\n'
                            'Sua escolha: '))
print('Obs: o arquivo será baixado no diretório atual.')

if escolha_usuario == '1':
    video = yt.streams.filter(only_audio=True).first()
    print(f'Baixando {titulo_do_video}...')
    arquivo_em_video = video.download()
    base, extensao = os.path.splitext(arquivo_em_video)
    arquivo_em_audio = base + '.mp3'
    os.rename(arquivo_em_video, arquivo_em_audio)
    '''
    Também poderia ser feito dessa forma, com o replace, desde que o arquivo fosse sempre em .mp4
    arquivo_em_audio = arquivo_em_video.replace('.mp4', '.mp3')
    os.rename(arquivo_em_video, arquivo_em_audio)
    '''
elif escolha_usuario == '2':
    stream = yt.streams.get_highest_resolution()
    print(f'Baixando {titulo_do_video}...')
    print(stream)
    stream.download()
