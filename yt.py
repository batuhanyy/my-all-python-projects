from pytube import YouTube
import os

def download_mp3(link):
    try:
        yt = YouTube(link)
    except:
        print("Bağlantı hatası")
        return

    # Get the audio stream with the highest quality available
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Get the title of the video and use it as the filename for the downloaded audio
    audio_filename = yt.title + ".mp3"

    # Set the download location to the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    try:
        audio_stream.download(output_path=desktop_path, filename=audio_filename)
        print("Audio dosyası başarıyla indirildi")
    except:
        print("İndirme sırasında hata oluştu")

def download_mp4(link):
    try:
        yt = YouTube(link)
    except:
        print("Bağlantı hatası")
        return

    # Get the video stream with the highest resolution (regardless of format)
    video_stream = yt.streams.get_highest_resolution()

    # Get the title of the video and use it as the filename for the downloaded video
    video_filename = yt.title + ".mp4"

    # Set the download location to the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    try:
        video_stream.download(output_path=desktop_path, filename=video_filename)
        print("Video dosyası başarıyla indirildi")
    except:
        print("İndirme sırasında hata oluştu")

def main():
    print("Hangi formatı indirmek istersiniz?")
    print("1. MP3")
    print("2. MP4")

    format_choice = input("Seçiminizi yapın (1 veya 2): ")
    link = input("Video linki: ")

    if format_choice == "1":
        download_mp3(link)
    elif format_choice == "2":
        download_mp4(link)
    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 girin.")

if __name__ == "__main__":
    main()
