class PowerManager:
    def __init__(self):
        self.active = True

    def turn_on(self):
        self.active = True
        print("[POWER] JARVIS turned ON")

    def turn_off(self):
        self.active = False
        print("[POWER] JARVIS turned OFF")

    def is_active(self):
        return self.active
