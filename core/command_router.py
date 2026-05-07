class CommandRouter:

    def route(self, command: str):

        command = command.lower()

        # ==========================================
        # SHUTDOWN
        # ==========================================
        shutdown_words = [
            "shutdown",
            "shut down",
            "go offline",
            "turn off"
        ]

        if any(word in command for word in shutdown_words):
            return "SHUTDOWN"

        # ==========================================
        # OPEN COMMANDS
        # ==========================================
        open_words = [
            "open",
            "launch",
            "start",
            "run"
        ]

        if any(word in command for word in open_words):
            return "OPEN_COMMAND"

        # ==========================================
        # SEARCH / AI / QUESTIONS
        # ==========================================
        search_words = [

            "search",
            "find",
            "who is",
            "what is",
            "what are",
            "tell me about",
            "explain",
            "youtube",
            "watch",
            "play",
            "amazon",
            "buy",
            "music",
            "song",
            "tutorial"
        ]

        if any(word in command for word in search_words):
            return "SEARCH"

        # ==========================================
        # WEATHER
        # ==========================================
        if "weather" in command:
            return "WEATHER_QUERY"

        # ==========================================
        # SYSTEM
        # ==========================================
        if any(word in command for word in [
            "system",
            "status",
            "battery",
            "cpu",
            "ram"
        ]):
            return "SYSTEM_QUERY"

        return "UNKNOWN"