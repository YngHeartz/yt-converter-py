import os
from pytube import YouTube
from pydub import AudioSegment

def youtubeDownloader():
    link = input("Enter the YouTube link to download: ")

    if not link:
        print("No Link Entered")
        return

    print("Choose format to download:")
    print("1. Video")
    print("2. Audio")

    choice = input("Enter the number of your choice: ")

    if choice not in ['1', '2']:
        print("Invalid choice")
        return

    try:
        yt = YouTube(link)
        print(f"Title: {yt.title}")
        print("Downloading...")

        if choice == '1':
            ys = yt.streams.get_highest_resolution()
            folder = "Videos"
            file_extension = 'mp4'
        else:
            ys = yt.streams.filter(only_audio=True).first()
            folder = "Audio"
            file_extension = 'mp4'

        if not os.path.exists(folder):
            os.makedirs(folder)

        # Download the file
        temp_file = os.path.join(folder, f"temp.{file_extension}")
        ys.download(output_path=folder, filename=f"temp.{file_extension}")

        if choice == '2':
            # Choose audio format for conversion
            choice2Option = input('Which audio format would you like? Type 1 for MP3 and 2 for WAV: ')
            audio = AudioSegment.from_file(temp_file)

            if choice2Option == '1':
                mp3_file = os.path.join(folder, f"{yt.title}.mp3")
                audio.export(mp3_file, format='mp3')
                print(f"MP3 file saved in {folder}/")
            elif choice2Option == '2':
                wav_file = os.path.join(folder, f"{yt.title}.wav")
                audio.export(wav_file, format='wav')
                print(f"WAV file saved in {folder}/")
            else:
                print("Invalid choice for audio format")
                return

            os.remove(temp_file)  # Remove the temporary file

        else:
            print(f"Download completed! File saved in {folder}/")

    except Exception as e:
        print(f"An error occurred: {e}")

youtubeDownloader()