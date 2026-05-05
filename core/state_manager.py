from states.jarvis_states import JarvisState

class StateManager:
    def __init__(self):
        self.current_state = JarvisState.OFF
        self.listeners = []   # UI subscribers

    def set_state(self, new_state: JarvisState):
        print(f"[STATE] {self.current_state.name} → {new_state.name}")
        self.current_state = new_state

    # Notify all listeners (UI will hook here)
        for listener in self.listeners:
            listener(new_state)

    def get_state(self):
        return self.current_state
    def subscribe(self, listener):
        self.listeners.append(listener)