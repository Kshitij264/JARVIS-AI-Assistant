from states.jarvis_states import JarvisState

class StateManager:
    def __init__(self):
        self.current_state = JarvisState.OFF

    def set_state(self, new_state: JarvisState):
        print(f"[STATE] {self.current_state.name} → {new_state.name}")
        self.current_state = new_state

    def get_state(self):
        return self.current_state
