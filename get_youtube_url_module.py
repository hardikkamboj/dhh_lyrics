import youtube_dl
import json

def get_youtube_url(video_url, video_resolution):
    '''
    Gives the url of the youtube video in a format which is understnadable 
    for opencv

    input - url (string)
            url of the youtube video

            resolution (string)
            resolution of the required url
            eg. '144p' , '720p' etc
            
            for audio 
            > get_youtube_url(--url--, 'tiny')

    output - urls (list of urls wit the given resulution)
    '''

    ydl_opts = {}

    # create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)

    # get video formats available
    formats = info_dict.get('formats',None)
    
    urls = []
    for f in formats:

        # I want the lowest resolution, so I set resolution as 144p
        if f.get('format_note',None) == video_resolution:

            #get the video url
            url = f.get('url',None)

            # open url with opencv
            urls.append(url)

    return urls