from get_youtube_url_module import * 
from open_cv_module import *

URL = 'https://www.youtube.com/watch?v=lQy2e-aWTfY'

result = get_youtube_url(URL,'720p')
print(len(result))

play_video_from_url(result[0])
