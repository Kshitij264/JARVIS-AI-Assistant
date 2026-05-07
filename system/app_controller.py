import subprocess
import webbrowser
import os


class AppController:

    def __init__(self):

        # ==============================
        # APP DATABASE
        # ==============================
        self.apps = {

            # System Apps
            "notepad": "notepad",
            "calculator": "calc",
            "calc": "calc",
            "cmd": "cmd",
            "terminal": "cmd",
            "file explorer": "explorer",
            "explorer": "explorer",

            # Browsers
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "google chrome": "chrome",
            "edge": "msedge",
            "firefox": "firefox",
            "brave": "brave",

            # Development
            "vs code": r"C:\Users\kshit\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "visual studio code": r"C:\Users\kshit\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "vscode": r"C:\Users\kshit\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            # Communication
            "whatsapp": [
                "explorer",
                "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
            ],

            "telegram": "telegram",
            "discord": "discord",
            "teams": "teams",

            # Media
            "spotify": "spotify",
            "vlc": "vlc",

            # AI
            "chatgpt": "https://chat.openai.com",

            # Office
            "word": "winword",
            "excel": "excel",
            "powerpoint": "powerpnt"
        }

        # ==============================
        # WEBSITE DATABASE
        # ==============================
        self.websites = {

            "youtube": "https://www.youtube.com",
            "gmail": "https://mail.google.com",
            "linkedin": "https://www.linkedin.com",
            "github": "https://github.com",
            "chatgpt": "https://chat.openai.com",
            "outlook": "https://outlook.live.com",
            "netflix": "https://www.netflix.com",
            "spotify web": "https://open.spotify.com"
        }

    # ==================================================
    # CLEAN COMMAND
    # ==================================================
    def clean_command(self, command: str):

        command = command.lower()

        remove_words = [

            # assistant fillers
            "can you",
            "could you",
            "would you",
            "please",
            "jarvis",

            # app actions
            "open",
            "launch",
            "start",
            "run",

            # search actions
            "search",
            "find",
            "look up",
            "google",
            "search for",

            # youtube actions
            "play",
            "watch",

            # extra conversational junk
            "for me",
            "on google",
            "on youtube"
        ]

        for word in remove_words:
            command = command.replace(word, "")

        return command.strip()
    # ==================================================
    # OPEN APPLICATION
    # ==================================================
    def open_application(self, command: str):

        cleaned = self.clean_command(command)

        for app_name, app_exec in self.apps.items():

            if app_name in cleaned:

                try:

                    # WEBSITE APP
                    if isinstance(app_exec, str) and app_exec.startswith("http"):
                        webbrowser.open(app_exec)
                        return True

                    # WHATSAPP SPECIAL CASE
                    elif isinstance(app_exec, list):
                        subprocess.Popen(app_exec)
                        return True

                    # NORMAL EXECUTABLE
                    else:
                        subprocess.Popen(app_exec)
                        return True

                except Exception as e:
                    print(f"[APP ERROR] {e}")
                    return False

        # ==========================================
        # LAST RESORT:
        # Try Windows Start Search
        # ==========================================
        try:
            subprocess.Popen(cleaned)
            return True

        except:
            return False

    # ==================================================
    # OPEN WEBSITE
    # ==================================================
    def open_website(self, command: str):

        cleaned = self.clean_command(command)

        for site_name, url in self.websites.items():

            if site_name in cleaned:

                webbrowser.open(url)
                return True

        return False
        # ==================================================
    # YOUTUBE SEARCH
    # ==================================================
    def youtube_search(self, command: str):

        cleaned = self.clean_command(command)

        url = f"https://www.youtube.com/results?search_query={cleaned.replace(' ', '+')}"

        webbrowser.open(url)

        return True


    # ==================================================
    # SPOTIFY SEARCH
    # ==================================================
    def spotify_search(self, command: str):

        cleaned = self.clean_command(command)

        url = f"https://open.spotify.com/search/{cleaned}"

        webbrowser.open(url)

        return True


    # ==================================================
    # AMAZON SEARCH
    # ==================================================
    def amazon_search(self, command: str):

        cleaned = self.clean_command(command)

        url = f"https://www.amazon.in/s?k={cleaned.replace(' ', '+')}"

        webbrowser.open(url)

        return True
    # ==================================================
    # GOOGLE SEARCH FALLBACK
    # ==================================================
    def google_search(self, command: str):

        try:

            cleaned = self.clean_command(command)

            query = cleaned.replace(" ", "+")

            url = f"https://www.google.com/search?q={query}"

            webbrowser.open(url)

            return True

        except:
            return False