from moviepy import editor
video = editor.VideoFileClip('D:\EBook\Computer Learning\Python Edu\Python_Course\Assignment 7\iseeyou.mp4')
video.audio.write_audiofile('iseeyou.mp3')