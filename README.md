# Youtube Transcription Whisper

<br>
    <div>
        <a href="https://colab.research.google.com/github/dodoya1/youtube_transcription_whisper/blob/master/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
    </div>
<br>

## Description
"Youtube Transcription Whisper" is a Python script for transcribing YouTube videos. The user must enter the URL of the YouTube video to be subtitled and the name of the folder where the transcription results will be saved.

## Setup
Install this repository with the following command:

    git clone https://github.com/dodoya1/youtube_transcription_whisper.git

In order to execute this code, the required modules must be installed:

    pip install -r requirements.txt

It also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Usage
Execute main.py with the following command.

    python3 main.py

Next, enter the URL of the YouTube video to which you want to add subtitles. Additionally, you will need to enter the name of the folder where you want to save the output results.

When selecting a language, please refer to the "ISO-639 Code" on the following website.

https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

## Approach
This code is designed to download a video from a YouTube URL and generate a transcription of the audio in the video. The code uses the "yt-dlp" library to download the video from the given URL and save it in a folder specified by the user. Next, the "whisper" library is used to transcribe the audio from the video and generate a text file containing the transcribed audio.

The main function first prompts the user to enter the YouTube URL to which they wish to add subtitles and the name of the folder in which to save the output results. After creating the specified folder, the function downloads the video using the yt_dl module, transcribes the audio using the whisper library, and saves the resulting transcription as a text file in the specified folder.

## References
https://github.com/openai/whisper

https://tt-tsukumochi.com/archives/2028

## Contribute
Please share your ideas and opinions!	
### Bug Report
If you find a bug in the project, please submit a detailed bug report on the Issues page on Github. Please include steps to reproduce the problem, expected behavior, and actual behavior. Screenshots and error messages are also helpful.
### Feature Requests
If you have an idea for a new feature, please submit a feature request on the Issues page on Github. Please describe the feature in detail and how it will benefit the project. If possible, please provide examples or mockups.
### Pull Requests
We welcome pull requests from anyone who would like to contribute to the project. Fork the repository and create a new branch for your changes. Please ensure that your code conforms to our coding standards and include unit tests where appropriate. Once you submit a pull request, it will be reviewed by a maintainer.
### Documentation
We need help improving our project documentation. This includes adding to the README.md file, creating user guides, and updating inline code comments. To contribute to the documentation, please submit a pull request with your changes.
### Evaluation
We value the contributions of all contributors highly. If you submit a pull request and it is merged into the project, we will add you to the list of contributors in the README.md file. Additionally, if you contribute significantly to the project, we may invite you to become a maintainer.
