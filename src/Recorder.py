# from plyer import facades
# import os
# import platform

# def get_file_path():
#     # Tentukan lokasi penyimpanan file audio
#         if platform.system().lower() == 'windows':
#             file_path = os.path.join(os.getcwd(), 'src/', 'temp/', 'rekaman_audio.wav')
#         elif platform.system().lower() == 'android':
#         # Sesuaikan dengan path penyimpanan di Android
#             file_path = os.path.join(os.path.expanduser('~'), 'src', 'temp', 'rekaman_audio.wav')
        
#         return file_path
#         # Fungsi untuk merekam suara
# def record_audio(file_path):
#     # Inisialisasi objek Audio
#     audio_player = facades.Audio()

#     try:
#         # Memulai merekam audio
#         audio_player.start()

#         input("Tekan Enter untuk berhenti merekam...")

#         # Berhenti merekam audio
#         audio_player.stop()

#         # Simpan file audio
#         audio_player.save(file_path)
#         print(f"File audio disimpan di: {file_path}")

#     except Exception as e:
#         print(f"Terjadi kesalahan: {str(e)}")

# if __name__ == "__main__":
#     file_path = get_file_path()
   
from plyer import facades
import os
import platform

def get_file_path():
    # Tentukan lokasi penyimpanan file audio
    if platform.system().lower() == 'windows':
        file_path = os.path.join(os.getcwd(),'temp')
    elif platform.system().lower() == 'android':
        # Sesuaikan dengan path penyimpanan di Android
        file_path = os.path.join(os.path.expanduser('~'), 'temp')
    else:
        # Default path for other platforms
        file_path = os.path.join(os.getcwd(), 'temp')

    return file_path

# Fungsi untuk merekam suara
def record_audio(file_path):
    # Inisialisasi objek Audio
    audio_player = facades.Audio()

    try:
        # Memulai merekam audio
        audio_player.start()

        input("Tekan Enter untuk berhenti merekam...")

        # Berhenti merekam audio
        audio_player.stop()

        # Simpan file audio
        audio_player.save(file_path)
        print(f"File audio disimpan di: {file_path}")

    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    file_path = get_file_path()
    record_audio(file_path)

    