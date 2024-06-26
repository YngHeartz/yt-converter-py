# Dealing with the file system of app
import os
# How we interact with the youtube api
from pytube import YouTube

def youtubeDownloader():
    # How we get the link to the youtube video
    link = input("Enter the YouTube link to download: ")
    
    # Error handling
    if not link:
        print("No Link Entered")
        return
    
    # If we have a youtube video provide this option to the user
    print("Choose format to download:")
    print("1. Video")
    print("2. Audio")
    
    # Get the choice from the user and assign it to choice variable
    choice = input("Enter the number of your choice: ")

    # Error Handling if not valid option
    if choice not in ['1', '2']:
        print("Invalid choice")
        return

    # tries to get the youtube video from the youtube api if the choice is 1 it will download the video in the highest resolution. If the chouce is 2 it will download the video in the audio version only.
    try:
        yt = YouTube(link)
        print(f"Title: {yt.title}")
        print("Downloading...")

        if choice == '1':
            # Select the highest resolution video stream
            ys = yt.streams.get_highest_resolution()
            folder = "Videos"
        else:
            # Select the audio stream
            ys = yt.streams.filter(only_audio=True).first()
            folder = "Audio"

        # Create folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Download the file
        ys.download(folder)
        
        # If the file is successfully downloaded send message to user about completion.
        print(f"Download completed! File saved in {folder}/")
    except Exception as e:
        # Error message if something went wrong.
        print(f"An error occurred: {e}")

youtubeDownloader()