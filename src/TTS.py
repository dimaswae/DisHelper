import os
import librosa
import soundfile as sf
from gtts import gTTS
from kivy.core.audio import SoundLoader

class TTSprotocol:
    @staticmethod
    def text_to_speech(text, nama_file='audio_file.wav', auto_play=True):
        try:
            # Ganti path sesuai dengan struktur direktori proyek
            absolute_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp')
            file_hasil = os.path.join(absolute_path, nama_file)

            tts = gTTS(text, lang='id')
            tts.save(file_hasil)

            # Menggunakan sr sebagai sample rate dari gTTS
            sr = 20000  # atau sr = 22050, tergantung pada kebutuhan Anda
            audio, sr = librosa.load(file_hasil)

            sf.write(file_hasil, audio, sr, subtype='PCM_16')

            if auto_play:
                TTSprotocol.play_audio(file_hasil)

            return file_hasil
        except Exception as e:
            print(f'Error: {str(e)}')
            return None

    @staticmethod
    def play_audio(audio_path='/src/temp/audio_file.wav'):
        sound = SoundLoader.load(audio_path)
        if sound:
            sound.play()
