from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip


class LyricsMaker:
    def __init__(self, lyrics, font_size, font_name, image_name):
        self.lyrics = lyrics
        self.font_size = font_size
        self.font_name = font_name 
        self.image_name = image_name
        self.font = ImageFont.truetype(font=self.font_name, size=self.font_size)
        self.image = Image.open(self.image_name)
        self.draw = ImageDraw.Draw(self.image)


    def convert_time_to_seconds(self, time_str):
        total_seconds = 0
        parts = time_str.split('-')
        
        for part in parts:
            minutes = 0
            seconds = 0
            
            if 'm' in part:
                m_split = part.split('m')
                minutes = int(m_split[0])
                if len(m_split) > 1 and 's' in m_split[1]:
                    seconds = float(m_split[1].replace('s', ''))
            elif 's' in part:
                seconds = float(part.replace('s', ''))
            total_seconds += minutes * 60 + seconds
        return total_seconds

    def convert_time_range(self, time_range):
        start, end = time_range.split('-')
        return self.convert_time_to_seconds(start), self.convert_time_to_seconds(end)

    def get_text_size(self, text):
        bbox = self.draw.textbbox((0, 0), text, font=self.font)
        letter_width = bbox[2] - bbox[0]
        letter_height = bbox[3] - bbox[1]
        return letter_width, letter_height

    def create_lyric_clips(self):
        clips = []
        for key, lines in self.lyrics.items():
            start, end = self.convert_time_range(key)
            second = end - start

            img = Image.open(self.image_name)
            draw = ImageDraw.Draw(img)
            width, height = img.size

            n = len(lines)
            for i, text in enumerate(lines, 1):
                w, h = self.get_text_size(text)
                draw.text((int(width-w)//2, int(height/3 - 150*((n/2)-i))), text, font=self.font, fill=(255, 255, 255))

            img.save("image_temp.png")
            clip = ImageClip("image_temp.png").set_duration(second)
            clips.append(clip)

        return clips

    def create_video(self, output_filename, audio_filename):
        clips = self.create_lyric_clips()
        final_clip = concatenate_videoclips(clips)
        audio = AudioFileClip(audio_filename)
        final_clip = final_clip.set_audio(audio)
        final_clip = final_clip.set_duration(audio.duration)
        final_clip.write_videofile(output_filename, fps=0.5)




lyrics = {
    "00-15s": ["Born In The Wild (Tems)" , "Lyrics By Stephene" ],
    "15.01s-22s": ["It's all over the news, all over the news" , "I notice, under the sun,", "strugglin' to find my focus"] , 
    "22.01s-27s": ["When I was young, younger", "My mind was always runnin' away"] , 
    "27.01s-41s": ["Up in the night, wishin' somebody knew me", "Something inside, pain in my mind, confused", "I didn't know why, didn't know why I could choose"], 
    "41.01s-50s": ["Born in the wild, born in the wild", 'Born in the wild, born in the wild'], 
    "50.01s-58s": ['I grew up in the wilderness', "Didn't know much about openness", ], 
    "58.01s-1m05s": ["Born in the wild, born in the wild", "Born in the wild, born in the wild"] , 
    "1m05.01s-1m12s": ["I was born in the wild, grew up in the wild, yeah", "You gave me my world"], 
    "1m12.01s-1m20s": ["And the world, the world is mine","The world is mine, the world, " , "the world is mine"],
    "1m20s.01s-1m27s": ["I need time, the time is now","The time is now, the time is now" ], 
    "1m27.01s-1m36s": ["For so long I was silent", "For you, giving more than I imagined", "Oh you, you're changing, no"] ,
    "1m35.01s-1m42s": ["All of my issues, all of my issues", "All of my issues", ], 
    "1m42.01s-1m57s": ["For so long I was silent", "Oh, you're givin' more than I imagined", "Oh, you gave me a new definition", "No inhibition, no more conditions" ],
    "1m57.01s-2m17s": ["Born in the wild, born in the wild", "Born in the wild"]
}


size = 150
font_name = "SIXTY.TTF"
image_name = "image.png"
lyrics_maker = LyricsMaker(lyrics, size, font_name,image_name)
lyrics_maker.create_video("BornInTheWild_Lyrics.mp4", "Tems-BornintheWild.mp3")
