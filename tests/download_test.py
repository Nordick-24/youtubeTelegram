from pytube import YouTube

youtube_video = YouTube(link)
youtube_video = youtube_video.streams.get_highest_resolution()

youtube_video.download(output_path="download_test/", filename="test.mp4")

