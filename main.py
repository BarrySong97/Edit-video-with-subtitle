import srt
from moviepy.video.io.VideoFileClip import VideoFileClip

srt_file = open("Modern.Family.S11E01.WEBRip.x264-ION10.srt", "r")

subs = list(srt.parse(srt_file))
# print(subs)
index = 2
# print(subs)
for item in subs:
  if index == 0:
    break
  start = srt.timedelta_to_srt_timestamp(item.start)
  end = srt.timedelta_to_srt_timestamp(item.end)
  video = VideoFileClip("Modern.Family.S11E01.WEBRip.x264-ION10.mp4").subclip(start, end)
  video.audio.write_audiofile("myHolidays_edited{0}.mp3".format(index))
  index -= 1
