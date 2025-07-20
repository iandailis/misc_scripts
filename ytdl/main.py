import yt_dlp
import sys

def main():
    if (len(sys.argv) != 2):
        print(f"usage: python3 {sys.argv[0]} <youtube_link_or_playlist>")
        return

    URLS = [sys.argv[1]]

    ydl_opts = {
        'format': 'opus/bestaudio/best',
        'restrictFilenames': True,
        'outtmpl': "download/%(artist)s - %(fulltitle)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio'
       }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)

if (__name__ == "__main__"):
    main()
