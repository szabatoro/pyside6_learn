import yt_dlp

def download(url, location, ph):
    ydl_opts = {
        'format': 'best', 
        'outtmpl': f'{location}/%(title)s.%(ext)s',
        'progress_hooks': [ph],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) 