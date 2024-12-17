# polymorphism in real world scenario

# Imagine kariye ek software application
# jo different types of media files ko
# play karta hai jaise audio files aur video files. Hum ek MediaPlayer class create kar sakte hain
# jo play method ko define karega, aur phir AudioPlayer aur VideoPlayer classes inherit karengi MediaPlayer class ko aur play method ko override
# karengi apne specific behavior ke liye.

# ------------------------------------------------------------------------------------------------------------

class MediaPlayer:
    def play(self):
        print ("Playing Media")

class AudioPlayer(MediaPlayer):
    def play(self):
        print ("Playing Audio File")

class VideoPlayer(MediaPlayer):
    def play(self):
        print ("Playing Video File")
    
media = MediaPlayer()
audio = AudioPlayer()
video = VideoPlayer()

media.play()
audio.play()
video.play()