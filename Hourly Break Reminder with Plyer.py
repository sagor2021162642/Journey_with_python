import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!",
            message = "Take break!\nIt has been an hour!",
        )
        time.sleep(3600)