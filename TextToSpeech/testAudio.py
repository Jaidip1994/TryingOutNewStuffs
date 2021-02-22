import io
import pygame
from gtts import gTTS

# To play audio text-to-speech during execution
def speak(my_text):
    with io.BytesIO() as f:
        gTTS(text=my_text, lang='en').write_to_fp(f)
        f.seek(0)
        print(f.name)
        pygame.mixer.init()
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
strval = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
strrval2 = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. " 
strrval3 = "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
speak(strval)
speak(strrval2)
speak(strrval3)


# Try in Google Colab/Jupyter Notebook
# from IPython.display import Audio
# from gtts import gTTS
# from tempfile import TemporaryFile

# # To play audio text-to-speech during execution
# def speak(my_text):
#     with io.BytesIO() as f:
#         gTTS(text=my_text, lang='en').write_to_fp(f)
#         f.seek(0)
#         return Audio(f.read(), autoplay=True)

# speak('checkpoint number one : Packages and modules successfully imported')