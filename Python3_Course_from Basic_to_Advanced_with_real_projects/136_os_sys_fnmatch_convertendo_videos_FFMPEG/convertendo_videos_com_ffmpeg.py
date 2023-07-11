"""
https://ffmpeg.org/documentation.html

Entendendo o comando:

- chamar o ffmpeg;
- chamar um arquivo de (-i "ENTRADA");
- Se existir um arquivo de legenda nos chamamos também (-i "LEGENDA");
- Informat o codec de vídeo (-c:v libx264);
- chamar o controle de qualidade (-crf 23);
- (-preset);
- ultrafast para acelerar;
- Informar o codec de áudio (-c:a aac);
- Mudar bitrate de áudio (-b:a 320k)
- Se for utilizada legenda, utilizar o codec de legendas
(-c:s srt -map V:0 a -map 1:0 -SS 00:00:00 -to 00:00:10 "SAIDA");
*** Convertendo somente 10 segundos de vídeo ***

- Para converter, temos que criar um pasta ffmepg na pasta de projeto e inserir o arquivo .exe nela (Windows)
"""
import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'C:\Users\wmare\Desktop\Curso_Atual\136_os_sys_fnmatch_convertendo_videos_FFMPEG\ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset fast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'
debug = ''

caminho_origem = r'C:\Users\wmare\Videos'
caminho_destino = r'C:\Users\wmare\Videos'


for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mpg'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
            f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
