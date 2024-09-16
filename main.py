from moviepy.editor import *
import os

def create_video_from_images(image_folder, output_file, image_durations):

    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
    
    clips = []
    for img, duration in zip(image_files, image_durations):
        clip = ImageClip(os.path.join(image_folder, img)).set_duration(duration)
        clips.append(clip)
    
    # Concatenate all the clips
    final_clip = concatenate_videoclips(clips, method="compose")
    
    # Write the result to a file
    final_clip.write_videofile(output_file, fps=24)

# Example usage
image_folder = "path/to/your/image/folder"
output_file = "output_video.mp4"
image_durations = [3, 5, 4, 2, 6]  # Duration in seconds for each image

create_video_from_images(image_folder, output_file, image_durations)


