from moviepy.editor import VideoFileClip

def convert_video_to_gif(video_path, gif_path, duration=10, fps=10):
    video = VideoFileClip(video_path).subclip(0, duration)
    video.write_gif(gif_path, fps=fps)

# Usage
convert_video_to_gif("BornInTheWild_Lyrics.mp4", "lyric_video_demo.gif")
