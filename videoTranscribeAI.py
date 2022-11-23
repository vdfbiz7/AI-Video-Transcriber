#Python program we are going to transcribe a Youtube video to text with the help of AI.

#Needed the installation of pytube and whisper
## pip3 install pytube
## pip3 install whisper

#Also in the case of ubuntu, needed the ffmpeg
##pip install ffmpeg-python

#import the dependencies needed
import pytube
import whisper

#import dependecies for checking and timer
import requests
from threading import Thread,Event
import time
import os

#Welcome to the transciber prints
def welcome():
    print("##########################################")
    print("#                                        #")
    print("#   Welcome to the videoTranscriber!     #")
    print("#                                        #")
    print("##########################################")
    print()
    print("Below are two links to the Youtube video as an example for the transcriber.")
    print("# ENGLISH: Al Pacino speech - Any Given Sunday  -> https://www.youtube.com/watch?v=f1yWSePMqsk")
    print("# SPANISH: Discurso sobre la vida - El Indomable Will Hunting -> https://www.youtube.com/watch?v=Js4mmRWCsic")
    print()

def check_video_url(video_id):
    checker_url = "https://www.youtube.com/oembed?url="
    video_url = checker_url + video_id
    request = requests.get(video_url)
    return request.status_code == 200

#Class for the timer shown runnign in other thread
class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        time=0
        while not self.stopped.wait(1):
            time=time+1
            transcurredTime="Time Transcurred: "+ str(time) + " seconds"
            print(transcurredTime, end='\r')
        print()

welcome()

#Ask for the link of the video we want to transcribe
youtubeVideoLink = input("Please enter the Youtube Link of the video you want to transcribe: ")

#Check that this video is valid
isVideoValid=check_video_url(youtubeVideoLink)
if not isVideoValid:
    print()
    print("Your video LINK is NOT valid! Program will close!")
    quit()

# Print the information that the transcription process has started 
# Also, start the total time counter, as well as the real timer thread
print()
print("You link is valid: " + youtubeVideoLink)
print("The transcription procees is starting....")
print()
# record start time
start = time.time()
#Set up the timer
stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()

#The transcription model is set
model =whisper.load_model('small')

#btain the video and get the audio.
youtubeVideo=pytube.YouTube(youtubeVideoLink)
audioYoutubeVideo=youtubeVideo.streams.get_audio_only()
#Audio is downloaded in a temp file
audioYoutubeVideo.download(filename='audioTemp.mp4')

result = model.transcribe('audioTemp.mp4')
transcription=result["text"]

# this will stop the timer
stopFlag.set()
# record end time
end = time.time()

#The total time and the result is print
print("The process has taken " + str(end-start) + "seconds")
print()
print("The transcription result is: ")
print(transcription)

print()
print("The transcription process has finished!")
print()

#Ask if want to save the transcription in a file
isPrint = input('Do you want to print the result in a .txt? (y/n): ').lower().strip() == 'y'

if isPrint:
    with open("OutputTranscription.txt", "w") as text_file:
        text_file.write(transcription)

#Ask if want to delete the temporal downloaded video
isVideoDeleted= input('Do you want to delete the temporal downloaded video? (y/n): ').lower().strip() == 'y'
if isVideoDeleted:
    os.remove("audioTemp.mp4")

print()
print("Program will close! See you soon!")