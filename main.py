from core.state_manager import StateManager
from core.command_router import CommandRouter
from core.response_engine import ResponseEngine
from states.jarvis_states import JarvisState
from system.app_controller import AppController
from system.voice_engine import VoiceEngine


def main():
    state_manager = StateManager()
    command_router = CommandRouter()
    response_engine = ResponseEngine()
    app_controller = AppController()
    voice_engine = VoiceEngine()

    print("JARVIS initialized.")
    state_manager.set_state(JarvisState.OFF)

    while True:

        # ==============================
        # OFF STATE (WAIT FOR ENTER)
        # ==============================
        if state_manager.get_state() == JarvisState.OFF:
            input("\nPress ENTER to activate JARVIS...")
            state_manager.set_state(JarvisState.IDLE)

            # Greeting
            state_manager.set_state(JarvisState.SPEAKING)
            greeting = "Hi Kshitij, how can I help you today?"
            print(f"JARVIS: {greeting}")
            voice_engine.speak(greeting)
            state_manager.set_state(JarvisState.IDLE)

        # ==============================
        # ON STATE (VOICE LOOP)
        # ==============================
        while state_manager.get_state() != JarvisState.OFF:

            command = voice_engine.listen()

            if not command:
                continue

            state_manager.set_state(JarvisState.THINKING)
            action = command_router.route(command)

            # ------------------------------
            # SHUTDOWN COMMAND
            # ------------------------------
            if action == "SHUTDOWN":
                state_manager.set_state(JarvisState.SPEAKING)
                voice_engine.speak("Understood. Going offline.")
                state_manager.set_state(JarvisState.OFF)
                break

            # ------------------------------
            # OPEN COMMAND
            # ------------------------------
            elif action == "OPEN_COMMAND":
                opened = app_controller.open_application(command)
                if not opened:
                    opened = app_controller.open_website(command)

                state_manager.set_state(JarvisState.SPEAKING)
                if opened:
                    voice_engine.speak("Opening as instructed.")
                else:
                    voice_engine.speak("I could not find that application.")

            # ------------------------------
            # WEATHER
            # ------------------------------
            elif action == "WEATHER_QUERY":
                state_manager.set_state(JarvisState.SPEAKING)
                voice_engine.speak("Weather functionality is not implemented yet.")

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


if __name__ == "__main__":
    main()
