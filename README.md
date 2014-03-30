# RTMPTube

RTMPTube is a tool to create live stream events on YouTube by managing the RTMP stream that YouTube requires, using FFMPEG as a streaming backend.

The current implementation uses `dvgrab` as a method of capturing video from hardware inputs, but this can readily be changed.

Installation is trivial - a build of FFMPEG is included, but if you have your own build, or want to use a repo build, the path to the FFMPEG build can easily be changed in the `STREAM.py` file. However, you must ensure that it is compiled with support for libx264, as YouTube expects FLV-wrapped h264 video. If in doubt, use the provided build.

### Usage

Open `STREAM.py` file to begin the stream configuration wizard. All of the required values must match the ones on the YouTube Live Event Management page, on the Encoder tab.

You should only need to provide the Stream Name and the required resolution in order to start the stream - the stream URL should be acceptable at the default value.

### Notes and Wishlist

*   At this time, there is no system to automatically provide the backup stream that YouTube has support for. However, if you wish to provide a backup stream, it should be possible to run a second instance of and alter the stream URL from the default value to the backup URL. **[#4](https://github.com/calmcl1/RTMPTube/issues/4)**

*   There is currently no support for the creation of new live events purely through the Google APIs, but this is planned. **[#3](https://github.com/calmcl1/RTMPTube/issues/3)**

*   There is currently no support for automatically detecting the resolution of a stream through the Google APIs when a stream name has been provided, but this is planned. **[#2](https://github.com/calmcl1/RTMPTube/issues/2)**

* There is currently no support for toggling the PAL colour expansion, which is enabled by default, but this is planned. **[#1]((https://github.com/calmcl1/RTMPTube/issues/1)**

### Contact

If there are any issues with the software or there's anything that you'd particularly like me to look into, do please file a request at https://github.com/calmcl1/RTMPTube/issues