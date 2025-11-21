import platform

try:
    from winotify import Notification, audio
    USE_WIN = platform.system() == "Windows"
except:
    USE_WIN = False


def notify(title, message):
    if USE_WIN:
        try:
            toast = Notification(
                app_id="Network Watchdog",
                title=title,
                msg=message,
                duration="short"
            )
            toast.set_audio(audio.Default, loop=False)
            toast.show()
            return
        except:
            pass

    print(f"[NOTIFY] {title}: {message}")
