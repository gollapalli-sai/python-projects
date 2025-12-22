import yt_dlp

url = "https://www.youtube.com/watch?v=ltLTwjjTehg"

ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
