import sys
import threading

from PyQt5.QtWidgets import QApplication

from core.state_manager import StateManager
from core.command_router import CommandRouter
from core.response_engine import ResponseEngine
from states.jarvis_states import JarvisState
from system.app_controller import AppController
from ui.hud import JarvisHUD


# ==============================
# BACKEND LOOP (RUNS IN THREAD)
# ==============================
def run_jarvis(state_manager, command_router, app_controller):

    while True:

        # ==============================
        # OFF STATE
        # ==============================
        if state_manager.get_state() == JarvisState.OFF:
            input("\nPress ENTER to activate JARVIS...")
            state_manager.set_state(JarvisState.IDLE)

            state_manager.set_state(JarvisState.SPEAKING)
            greeting = "Hi Kshitij, how can I help you today?"
            print(f"JARVIS: {greeting}")
            state_manager.set_state(JarvisState.IDLE)

        # ==============================
        # ACTIVE LOOP
        # ==============================
        while state_manager.get_state() != JarvisState.OFF:

            command = input("You: ")

            if not command:
                continue

            state_manager.set_state(JarvisState.THINKING)
            action = command_router.route(command)

            # ------------------------------
            # SHUTDOWN
            # ------------------------------
            if action == "SHUTDOWN":
                state_manager.set_state(JarvisState.SPEAKING)
                print("JARVIS: Going offline.")
                state_manager.set_state(JarvisState.OFF)
                break

            # ------------------------------
            # OPEN
            # ------------------------------
            elif action == "OPEN_COMMAND":
                opened = app_controller.open_application(command)
                if not opened:
                    opened = app_controller.open_website(command)

                state_manager.set_state(JarvisState.SPEAKING)
                if opened:
                    print("JARVIS: Opening as instructed.")
                else:
                    print("JARVIS: Could not find that application.")

            # ------------------------------
            # WEATHER
            # ------------------------------
            elif action == "WEATHER_QUERY":
                state_manager.set_state(JarvisState.SPEAKING)
                print("JARVIS: Weather not implemented yet.")

            # ------------------------------
            # SYSTEM CHECK
            # ------------------------------
            elif action == "SYSTEM_QUERY":
                state_manager.set_state(JarvisState.SPEAKING)
                print("JARVIS: All systems are functioning normally.")

            # ------------------------------
            # UNKNOWN
            # ------------------------------
            else:
                state_manager.set_state(JarvisState.SPEAKING)
                print("JARVIS: I did not understand that command.")

            state_manager.set_state(JarvisState.IDLE)


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

    # Connect UI to state
    state_manager.subscribe(hud.state_signal.emit)

    print("JARVIS initialized.")
    state_manager.set_state(JarvisState.OFF)

    # Run backend in separate thread
    jarvis_thread = threading.Thread(
        target=run_jarvis,
        args=(state_manager, command_router, app_controller),
        daemon=True
    )
    jarvis_thread.start()

    # Start Qt event loop (CRITICAL)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()