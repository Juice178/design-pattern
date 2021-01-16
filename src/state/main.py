from time import sleep
from safe_frame import SafeFrame
from PyQt5.QtWidgets import QApplication


def main() -> None:
    app = QApplication([])
    frame = SafeFrame("State Sample")
    frame.show()
    app.exec_()
    while True:
        for hour in range(24):
            frame.set_clock(hour)
            try:
                sleep(1)
            except KeyboardInterrupt:
                pass

if __name__ == "__main__":
    main()