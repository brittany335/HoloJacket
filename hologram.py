# this program runs a video from a raspberry pi and uses the GPIO pins to control the video
# Created By Brittany Cohen
##############################################################################################

# PLEASE Note: stdin.write typically should not be used due to possible deadlock, as a replacement communication() should be used

#To communicate to the videoplayer softwear written in a different language then python so we need to run
#UNIX commands through a subprocesser. Popen opens the subprocess to start the video program
#PIPE allows us to communicate to the videoplayer softwear
from subprocess import Popen, PIPE

import time
import RPi.GPIO as GPIO
#path to the video file
my_video_file_path='/home/pi/green1.mp4'


#opening the videoplayer and opening the file,
#setting standard input to PIPE so that we can communicate with the program via GPIO pins, otherwise the default is keyboard
my_process=Popen(['player',my_video_File_path], stdin=PIPE, close_fds=True)

#setting up the GPIO numbering system. these pin numbers follow the lower-level numbering system defined by the Raspberry Pi’s Broadcom-chip brain.
GPIO.setmode(GPIO.BCM)

#setting the pin mode, the pins will be inputs because we are reading in data from our push buttons. They will also include the
#the internal pullup resistors for the push button to prevent shorting
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)


while True:
	#setting names to GPIO pins
	button_state=GPIO.input(17)
	button_state1=GPIO.input(22)

	#when the button is pressed the voltage going to zero
	# if the button is pressed (it equals zero) and we will write to the program to quite out of the video
	if button_state==False:
		print("quite video")
		my_process.stdin.write("q")
		# time delay for debouncing
		time.sleep(.09)

	# if the button1 is pressed (it equals zero) and we will write to the program to go full screen
	if button_state1==False:
		print("full video")

		my_process.stdin.write("fs")
		# time delay for debouncing
		time.sleep(5)
