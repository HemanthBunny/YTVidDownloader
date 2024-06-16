from pytube import YouTube

def download_youtube_video(url, save_path='.'):
    try:
        yt = YouTube(url)
        print(f'Title: {yt.title}')
        print(f'Number of views: {yt.views}')
        print(f'Length of video: {yt.length} seconds')
        print(f'Rating: {yt.rating}')

        # List available streams
        streams = yt.streams.filter(progressive=True).all()
        for i, stream in enumerate(streams):
            print(f"{i}. {stream.resolution} - {stream.mime_type}")

        # Ask the user to select the stream
        stream_index = int(input("Enter the number of the desired stream: "))
        ys = streams[stream_index]

        print('Downloading...')
        ys.download(save_path)
        print('Download completed!')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    url = input('Enter the YouTube video URL: ')
    save_path = input('Enter the path to save the video: ') or '.'
    download_youtube_video(url, save_path)
