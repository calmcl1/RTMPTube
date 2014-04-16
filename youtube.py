__author__ = 'Callum'

CLIENT_ID = "521486839374-bmfjjgp0u22kosq0d5coomc9bm301mrc.apps.googleusercontent.com"
CLIENT_SECRET = "ygeVxPdk5oBpn9zIoQJtoZcL"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

class YouTubeEventManager():
    def __init__(self):
        pass

    def getEventList(self):
        pass

    def createNewEvent(self):
        pass

class Event():
    def __init__(self):
        pass

    def addStreamToEvent(self,stream):
        assert isinstance(stream,Stream)

class Stream():
    def __init__(self):
        stream_name = None
        server_url_primary = None
        server_url_backup = None

    def createStream(self):
        pass

    def startStream(self):
        pass

    def stopStream(self):
        pass