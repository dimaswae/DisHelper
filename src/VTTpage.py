# # vttpage.py
# from kivymd.app import MDApp
# from kivymd.uix.button import MDRaisedButton
# from Recorder import record_audio, get_file_path
# from VTT import VTTProtocol
# from config import openai_api_key

# class VTTApp(MDApp):
#     def build(self):
#         self.button = MDRaisedButton(
#             text="Tekan dan tahan untuk merekam",
#             on_touch_down=self.start_recording,
#             on_touch_up=self.stop_recording
#         )
#         return self.button

#     def start_recording(self, instance, touch):
#         if self.button.collide_point(*touch.pos):
#             self.file_path = record_audio("rekaman_audio.wav")

#     def stop_recording(self, instance, touch):
#         if self.button.collide_point(*touch.pos):
#             vtt_protocol = VTTProtocol(openai_api_key)
#             result_text = vtt_protocol.transcribe(self.file_path)
#             print(f"Hasil transkripsi: {result_text}")

# if __name__ == "__main__":
#     VTTApp().run()
# VTTpage.py
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from Recorder import record_audio, get_file_path
from VTT import VTTProtocol
from config import openai_api_key

class VTTApp(MDApp):
    def build(self):
        self.button = MDRaisedButton(
            text="Tekan dan tahan untuk merekam",
            on_touch_down=self.start_recording,
            on_touch_up=self.stop_recording
        )
        return self.button

    def start_recording(self, instance, touch):
        file_path = get_file_path()
        if self.button.collide_point(*touch.pos):
            self.file_path = record_audio(file_path)

    def stop_recording(self, instance, touch):
        if self.button.collide_point(*touch.pos):
            vtt_protocol = VTTProtocol(api_key=openai_api_key)
            result_text = vtt_protocol.transcribe(self.file_path)
            print(f"Hasil transkripsi: {result_text}")

if __name__ == "__main__":
    VTTApp().run()
