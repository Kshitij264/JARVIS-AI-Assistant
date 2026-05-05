import speech_recognition as sr
from TTS.api import TTS
import sounddevice as sd
import soundfile as sf
import tempfile
import os


class VoiceEngine:
    def __init__(self):
        print("[VOICE] Loading Neural Male Voice Model... (First time may take 20-30 sec)")

        # Speech Recognition
        self.recognizer = sr.Recognizer()

        # Force correct microphone (Device 1 from your list)
        self.microphone = sr.Microphone(device_index=1)

        # Coqui TTS Model (Male Voice)
        self.tts = TTS(
            model_name="tts_models/en/vctk/vits",
            progress_bar=False,
            gpu=False
        )

        # Choose a male speaker from VCTK
        self.speaker = "p226"   # You can change later if needed

    # ==============================
    # LISTEN FUNCTION
    # ==============================
    def listen(self):
        try:
            with self.microphone as source:
                print("[VOICE] Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                print("[VOICE] Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)

            try:
                command = self.recognizer.recognize_google(audio)
                print(f"[VOICE] You said: {command}")
                return command

            except sr.UnknownValueError:
                print("[VOICE] Could not understand audio")
                return ""

            except sr.RequestError as e:
                print(f"[VOICE] Recognition service error: {e}")
                return ""

        except Exception as e:
            print(f"[VOICE] Microphone error: {e}")
            return ""

    # ==============================
    # SPEAK FUNCTION (Neural Male)
    # ==============================
    def speak(self, text: str):
        try:
            print(f"[JARVIS] {text}")

            # Generate temporary wav file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
                temp_path = tmpfile.name

            self.tts.tts_to_file(
                text=text,
                speaker=self.speaker,
                file_path=temp_path
            )

            # Play generated audio
            data, samplerate = sf.read(temp_path)
            sd.play(data, samplerate)
            sd.wait()

            # Remove temp file
            os.remove(temp_path)

        except Exception as e:
            print(f"[VOICE ERROR] {e}")
