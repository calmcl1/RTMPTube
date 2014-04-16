__author__ = 'Callum'

CLIENT_ID = "521486839374-bmfjjgp0u22kosq0d5coomc9bm301mrc.apps.googleusercontent.com"
CLIENT_SECRET = "ygeVxPdk5oBpn9zIoQJtoZcL"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

class YouTubeEventManager():
    """
    Handles Events through the YouTube API.

    This includes retrieving existing events, creating new ones,
    binding streams, etc.
    """
    def __init__(self):
        pass

    def get_event_list(self):
        """
        Retrieves all the scheduled live events created by a given channel.
        """
        pass

    def create_new_event(self):
        """
        Crates a new event under a given channel so that a stream can be
        bound to it.
        """
        pass

class Event():
    """
    A live event, as per the YouTube API. Potentially irrelevant or
    able to be refactored into YouTubeEventManager.
    """
    def __init__(self):
        pass

    def add_stream_to_event(self,stream):
        """
        Binds a Stream object to an Event.
        """
        assert isinstance(stream,Stream)

class Stream():
    def __init__(self):
        stream_name = None
        server_url_primary = None
        server_url_backup = None

    def create_stream(self):
        """
        Creates a new Stream and registers it on the YT servers with given
        parameters.
        """
        pass

    def preview_stream(self):
        """
        Sets the stream to 'preview' mode.
        """
        pass

    def start_stream(self):
        """
        Makes the stream live.
        """
        pass

    def stop_stream(self):
        """
        Terminates a stream broadcast.
        """
        pass