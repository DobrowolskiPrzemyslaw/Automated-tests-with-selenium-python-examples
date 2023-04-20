from pytube import YouTube
from pytube.exceptions import VideoUnavailable

url='https://www.youtube.com/watch?v=Ypah0hnNa8Y'
download_dir = 'C:/Users/User/Music/YT'

try:
    yt = YouTube(url)
    filename = 'yt_record.mp3'
    print("Success downloading")
except VideoUnavailable:
    print(f'Video {url} is unavaialable, skipping.')
else:
    print(f'Downloading video')
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=download_dir, filename=filename)
    print(f'Success downloading video')