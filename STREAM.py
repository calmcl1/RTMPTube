# This software manages the 2UBE/2UBE Extra streaming to YouTube from the
# Catalyst Mac via dvgrab and ffmpeg.

# Author: Callum McLean
# Version: 1.1
# Changelog:
#	1.1: Added default fullscreen, opening instructions
#	1.0: Initial version

import subprocess

PATH_TO_FFMPEG = "/home/ubuntu/Desktop/ffmpeg"

# Video resolution presets
resolution_presets = {
    "1080p": {
        "res_h": "1920",
        "res_v": "1080",
        "bitrate": "4500"
    },
    "720p": {
        "res_h": "1280",
        "res_v": "720",
        "bitrate": "2500",
    },
    "480p": {
        "res_h": "854",
        "res_v": "480",
        "bitrate": "1000",
    },
    "360p": {
        "res_h": "640",
        "res_v": "360",
        "bitrate": "750",
    },
    "240p": {
        "res_h": "426",
        "res_v": "240",
        "bitrate": "400",
    }
}

resolution = stream_name = stream_url = None

print """2UBE Extra Stream Provider
Version 1.1 - 18/03/14

Press CTRL + C at any time to exit this programme and terminate the stream.

Use CTRL + SHIFT + C to copy and CTRL + SHIFT + V to paste.

"""

# Begin data entry part
print "Please provide the following data. Press Enter to accept defaults."

# Request the stream ID (second part of rtmp URL)
while not stream_name:
    stream_name = raw_input("Stream Name: ")
    if not stream_name: print "Sorry, try again."

# Request the stream base URL
stream_url = raw_input("Primary Server URL [default: rtmp://a.rtmp.youtube.com/live2]: ")
if not stream_url: stream_url = "rtmp://a.rtmp.youtube.com/live2"


# Request desired resolution
print """Available resolutions:
\t1. 1080p
\t2. 720p
\t3. 480p
\t4. 360p
\t5. 240p"""

res_input = None
while not res_input in ["1","2","3","4","5"]:
    res_input = raw_input("Resolution (1/2/3/4/5) [default: 720p]: ")
    if not res_input: res_input = "2"
    elif not res_input in ["1","2","3","4","5"]: "Sorry, try again."

if res_input == "1":
    resolution = resolution_presets["1080p"]
elif res_input == "2":
    resolution = resolution_presets["720p"]
elif res_input == "3":
    resolution = resolution_presets["480p"]
elif res_input == "4":
    resolution = resolution_presets["360p"]
elif res_input == "5":
    resolution = resolution_presets["240p"]

# Display the final stream settings

print """
Broadcast parameters:
\tResolution: %sx%s
\tVideo bitrate: %s
\tAudio bitrate: 192kbps
\tVideo codec: h264 (libx264)
\tAudio codec: aac
\tStream container: flv
\tGOP length: 15
\tFPS: 30

\tServer URL: %s
\tStream name: %s
""" % (resolution["res_h"],resolution["res_v"],
                    resolution["bitrate"] + "kbps", stream_url, stream_name)

# Approve the stream settings
raw_input("Press Enter to accept the settings and begin the stream.")

# Build the command
command = "dvgrab - | " + PATH_TO_FFMPEG + " -itsoffset:0 0.15 -i - -s " + resolution["res_h"] + "x"
command += resolution["res_v"] + " -b:v " + resolution["bitrate"] + "k -r 30 -ar 44100 -ab 192k "
command += '-f flv -c:v libx264 -aspect 16:9 -vf lutyuv="y=(val-16)*(255/219)" -c:a aac -strict experimental -g 15 '
command += stream_url + "/" + stream_name

# Start the stream
subprocess.call(command, shell=True)

# Ideal command:
#dvgrab - | PATH_TO_FFMPEG -ik - -s 1080x720 -b 3000k -ar 44100 -ab 128k -f flv -vcodec libx264 -acodec aac -strict experimental -g 15 -r 30 rtmp://a.rtmp.youtube.com/live2/the2ubeLIPA.fuas-hqvr-gzwu-7gyd
