import moviepy.editor

cvt_video=moviepy.editor.VideoFileClip("HELLO HEY")
ext_audio=cvt_video.audio
ext_audio.write_audiofile("audio_extracted.mp3")


