import speech_recognition as sr
from TTS.api import TTS
import sounddevice as sd
import soundfile as sf
import tempfile
import os

WAKE_WORDS = [
    "jarvis",
    "hey jarvis",
    "ok jarvis"
]
class VoiceEngine:
    def __init__(self):
        print("[VOICE] Loading Neural Male Voice Model... (First time may take 20-30 sec)")

        # Speech Recognition
        self.recognizer = sr.Recognizer()
        # Recognition tuning
        self.recognizer.energy_threshold = 80
        self.recognizer.dynamic_energy_threshold = False
        self.recognizer.pause_threshold = 0.8
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.5
        print("\n========== AVAILABLE MICROPHONES ==========")

        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"{index}: {name}")

        print("==========================================\n")

        # TEMP DEFAULT MIC
        print("\n========== AVAILABLE MICROPHONES ==========")

        mic_list = sr.Microphone.list_microphone_names()

        for index, name in enumerate(mic_list):
            print(f"{index}: {name}")

        print("==========================================\n")

        # CHANGE INDEX AFTER CHECKING TERMINAL
        self.microphone = sr.Microphone(device_index=0)
        # One-time ambient calibration
        with self.microphone as source:
            print("[VOICE] Calibrating microphone...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
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
                pass

                print("[VOICE] Listening...")
                print("[WAKE] Waiting for speech...")
                audio = self.recognizer.listen(
    source,
    timeout=4,
    phrase_time_limit=8
)

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
            print(f"[VOICE ERROR] {e}")
            return ""

        # ==============================
    # WAKE WORD LISTENER
    # ==============================
    def listen_for_wake_word(self):
        print("[WAKE] Listening for wake word...")
        try:

            with self.microphone as source:

                pass

                audio = self.recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=3
                )

            text = self.recognizer.recognize_google(audio).lower()

            print(f"[WAKE HEARD] {text}")

            return any(word in text for word in WAKE_WORDS)

        except Exception as e:
            print(f"[WAKE ERROR] {e}")
            return False


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
