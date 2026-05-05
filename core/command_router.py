class CommandRouter:
    def __init__(self):
        pass

    def route(self, command: str):
        command = command.lower()

        if "open" in command:
            return "OPEN_COMMAND"

        if "play" in command:
            return "PLAY_COMMAND"

        if "weather" in command:
            return "WEATHER_QUERY"

        if "system check" in command:
            return "SYSTEM_QUERY"

        if "shut down" in command or "shutdown" in command:
            return "SHUTDOWN"

        return "UNKNOWN"
