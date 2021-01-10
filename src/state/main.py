from time import sleep
from safe_frame import SafeFrame
def main() -> None:
    frame = SafeFrame("State Sample")
    while True:
        for hour in range(24):
            frame.set_clock(hour)
            try:
                sleep(1)
            except KeyboardInterrupt:
                pass