import yt_dlp

def download(url, title, dir):
    ydl_opts = {
        'outtmpl': f'{dir}/{title}.%(ext)s',
        'retries': 10,
        'external_downloader': 'aria2c',
        'external_downloader_args': ['-x', '16', '-s', '16']
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
