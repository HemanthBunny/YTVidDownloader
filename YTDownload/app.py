from flask import Flask, request, render_template
from pytube import YouTube
import io
from flask import send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            streams = yt.streams.filter(progressive=True).all()
            audio_streams = yt.streams.filter(only_audio=True).all()
            return render_template('index.html', streams=streams, audio_streams=audio_streams, yt=yt)
        except Exception as e:
            return str(e)
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    itag = request.form['itag']
    try:
        yt = YouTube(url)
        stream = yt.streams.get_by_itag(itag)

        buffer = io.BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        return send_file(buffer, as_attachment=True, download_name=f"{stream.title}.mp4", mimetype='video/mp4')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True, host= '192.168.1.6')
