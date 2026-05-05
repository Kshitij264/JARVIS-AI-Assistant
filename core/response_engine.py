class ResponseEngine:
    def respond(self, intent: str):
        responses = {
            "OPEN_COMMAND": "Opening as instructed.",
            "PLAY_COMMAND": "Playing the requested media.",
            "WEATHER_QUERY": "Fetching the latest weather update.",
            "SYSTEM_QUERY": "Running a quick system check.",
            "SHUTDOWN": "Understood. Shutting down now.",
            "UNKNOWN": "I did not understand that command."
        }

        return responses.get(intent, "Something went wrong.")
