from openai import OpenAI
from config import openai_api_key
from Recorder import get_file_path
import platform
import os

class VTTProtocol:
    def __init__(self, api_key = openai_api_key ) -> None:
        # self.client = OpenAI(api_key = openai_api_key
        self.api_key = api_key

    def transcribe(self, file_path):
        if self.api_key is None:
            raise ValueError("API key not set. Pass the API key to the constructor or use set_api_key(api_key) method.")
        file_path = get_file_path()
        audio_file = open(file_path, "rb")
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        return transcript
        pass
if __name__ == "__main__":
    vtt_protocol = VTTProtocol(openai_api_key)
    file_path = "rekaman_audio.wav"
    result_text = vtt_protocol.transcribe(file_path)
    print(result_text)