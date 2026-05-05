import subprocess
import webbrowser

class AppController:
    def open_application(self, command: str):
        command = command.lower()
        normalized = command.replace(" ", "")

        apps = {
            "notepad": ["notepad"],
            "calculator": ["calc"],
            "cmd": ["cmd"],
            "fileexplorer": ["explorer"],

            # Visual Studio Code
            "visualstudiocode": [
                r"C:\Users\kshit\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            ],

            # WhatsApp Desktop App ONLY
            "whatsapp": [
                "explorer",
                "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
            ]
        }

        for name, exec_cmd in apps.items():
            if name in normalized:
                try:
                    subprocess.Popen(exec_cmd)
                    return True
                except Exception as e:
                    print(f"[ERROR] Could not open {name}: {e}")
                    return False

        return False

    def open_website(self, command: str):
        command = command.lower()
        normalized = command.replace(" ", "")

        websites = {
            "youtube": "https://www.youtube.com",
            "linkedin": "https://www.linkedin.com",
            "gmail": "https://mail.google.com",
            "chatgpt": "https://chat.openai.com",
            "outlook": "https://outlook.live.com"
        }

        for name, url in websites.items():
            if name in normalized:
                webbrowser.open(url)
                return True

        return False
