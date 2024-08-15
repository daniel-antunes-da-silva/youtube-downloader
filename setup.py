# SCRIPT PARA CRIAR EXECUTÁVEL
from cx_Freeze import setup, Executable

# Definir o q deve ser incluído na pasta final
arquivos = ['widget.py']

# Saída de arquivos
configuracao = Executable(
    script='downloader.py'
)
# Configurar o executável
setup(
    name='YTB Downloader',
    version='2.0',
    description='Este programa baixa vídeos e áudios do Youtube.',
    author='Daniel Antunes',
    options={'build_exe': {
        'include_files': arquivos,
        'include_msvcr': True  # importante para rodar no WINDOWS.
        #'packages': ['funcoes']
    }},
    executables=[configuracao]
)
