import sys
import threading
import time

from PyQt5.QtWidgets import QApplication

from core.state_manager import StateManager
from core.command_router import CommandRouter
from core.response_engine import ResponseEngine
from states.jarvis_states import JarvisState
from system.app_controller import AppController
from system.voice_engine import VoiceEngine
from ui.hud import JarvisHUD
from system.voice_engine import VoiceEngine
# ==============================
# SESSION CONTROL
# ==============================
SESSION_TIMEOUT = 20

last_activity_time = time.time()
# ==============================
# UNIVERSAL COMMAND PROCESSOR
# ==============================
def process_command(
    command,
    state_manager,
    command_router,
    app_controller,
    voice_engine
):

    if not command:
        return

    print(f"[COMMAND RECEIVED] {command}")

    global last_activity_time
    last_activity_time = time.time()
    state_manager.set_state(JarvisState.THINKING)

    action = command_router.route(command)

    # ------------------------------
    # SHUTDOWN
    # ------------------------------
    if action == "SHUTDOWN":

        state_manager.set_state(JarvisState.SPEAKING)

        voice_engine.speak("Going offline.")

        state_manager.set_state(JarvisState.OFF)
        time.sleep(1)
        return

    # ------------------------------
    # OPEN
    # ------------------------------
    elif action == "OPEN_COMMAND":

        state_manager.set_state(JarvisState.EXECUTING)

        opened = app_controller.open_application(command)

        if not opened:
            opened = app_controller.open_website(command)

        state_manager.set_state(JarvisState.SPEAKING)

        if opened:
            voice_engine.speak("Opening as instructed.")
        else:
            voice_engine.speak("Could not find that application.")

    # ------------------------------
    # WEATHER
    # ------------------------------
    elif action == "WEATHER_QUERY":

        state_manager.set_state(JarvisState.SPEAKING)

        voice_engine.speak("Weather not implemented yet.")

    # ------------------------------
    # SYSTEM CHECK
    # ------------------------------
    elif action == "SYSTEM_QUERY":

        state_manager.set_state(JarvisState.SPEAKING)

        voice_engine.speak("All systems are functioning normally.")

    # ------------------------------
    # UNKNOWN
    # ------------------------------
    else:

        state_manager.set_state(JarvisState.SPEAKING)

        voice_engine.speak("I did not understand that command.")

    state_manager.set_state(JarvisState.IDLE)

# ==============================
# BACKEND LOOP (RUNS IN THREAD)
# ==============================
def run_jarvis(state_manager, command_router, app_controller, voice_engine):
    global last_activity_time
    while True:

                        # ==============================
        # OFF STATE (WAKE WORD MODE)
        # ==============================
        if state_manager.get_state() == JarvisState.OFF:

            activated = voice_engine.listen_for_wake_word()

            if not activated:
                continue

            last_activity_time = time.time()

            state_manager.set_state(JarvisState.SPEAKING)

            greeting = "Yes Kshitij?"

            print(f"JARVIS: {greeting}")

            voice_engine.speak(greeting)

            state_manager.set_state(JarvisState.IDLE)

            # IMPORTANT
            time.sleep(0.5)

            continue

        else:

            # Auto sleep
            if time.time() - last_activity_time > SESSION_TIMEOUT:

                print("[SESSION] Timeout reached.")

                state_manager.set_state(JarvisState.OFF)

                continue

            # Active listening
            state_manager.set_state(JarvisState.LISTENING)

            command = voice_engine.listen()

            if not command:

                state_manager.set_state(JarvisState.IDLE)

                continue

            process_command(
                command,
                state_manager,
                command_router,
                app_controller,
                voice_engine
            )                   
# ==============================
# MAIN (UI THREAD)
# ==============================
def main():
    app = QApplication(sys.argv)

    # UI
    hud = JarvisHUD()
    hud.show()

    # Core systems
    state_manager = StateManager()
    command_router = CommandRouter()
    app_controller = AppController()
    voice_engine = VoiceEngine()

    # Connect UI to state
    state_manager.subscribe(hud.state_signal.emit)

    print("JARVIS initialized.")
    state_manager.set_state(JarvisState.OFF)

    # Run backend in separate thread
    jarvis_thread = threading.Thread(
        target=run_jarvis,
        args=(state_manager, command_router, app_controller, voice_engine),
        daemon=True
    )
    jarvis_thread.start()
       

    # Start Qt event loop (CRITICAL)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()