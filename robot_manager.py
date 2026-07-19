import threading
import time

class RobotManager:

    def __init__(
        self,
        signal_engine,
        trade_executor
    ):

        self.running = False

        self.signal_engine = signal_engine

        self.trade_executor = trade_executor

    def start(self):

        self.running = True

        thread = threading.Thread(
            target=self.loop
        )

        thread.start()

    def stop(self):

        self.running = False

    def loop(self):

        while self.running:

            print(
                "Robot scanning market..."
            )

            time.sleep(60)
