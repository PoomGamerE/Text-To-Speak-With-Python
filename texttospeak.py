from gtts import gTTS
import playsound

tts = gTTS(text='ระบบสังเคราะห์เสียงด้วยไพธอน', lang='th', slow=False)
tts.save("output.mp3")

playsound.playsound("output.mp3", True)
