import whisper
from deep_translator import GoogleTranslator
import os

# Download the video from the given YouTube URL.
def yt_download(URL, result_folder_path):
    path = f"{result_folder_path}/target.mp4"
    # Download the video
    os.system(f"yt-dlp -f best -v {URL} -o {path}")

def main():
    URL = input("Enter the YouTube URL to which you want to add subtitles:")
    result_folder_name = str(input("Specify the name of the folder in which to save the output results:"))

    # Folder name to save output results
    result_folder_path = f"./result/{result_folder_name}"
    os.mkdir(result_folder_path)

    # Download the YouTube video using the yt_dl module.
    yt_download(URL, result_folder_path)

    model = whisper.load_model("medium")
    result = model.transcribe(f"{result_folder_path}/target.mp4")

    # Save the transcription as a text file.
    with open(f"{result_folder_path}/transcript.txt", mode = "w") as f:
        f.write(result["text"])

if __name__ == "__main__":
    main()
    