from get_youtube_url_module import * 
from open_cv_module import *
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", default=None,
	help="path to input image")

ap.add_argument("-v", "--video", default="fall_off.mp4",
	help="path to input image")

ap.add_argument
args = vars(ap.parse_args())

if args["url"]:
    URL = args["url"]
    play_video(URL)

else: 
    play_video(args["video"])
 
