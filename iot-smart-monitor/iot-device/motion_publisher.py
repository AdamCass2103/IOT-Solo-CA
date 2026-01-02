# iot-device/motion_publisher.py
import time
import random
from datetime import datetime
# from pubnub.pnconfiguration import PNConfiguration
# from pubnub.pubnub import PubNub
from config import MOTION_CHANNEL

def publish_motion():
    """
    Simulate motion detection event.
    Currently just prints to console.
    """
    while True:
        motion_detected = random.choice([True, False])  # Randomly detect motion
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if motion_detected:
            print(f"[{timestamp}] Motion detected!")
            # Later: Publish to PubNub
            # pubnub.publish().channel(MOTION_CHANNEL).message({"detected": True, "timestamp": timestamp}).sync()
        else:
            print(f"[{timestamp}] No motion.")

        time.sleep(5)  # Wait 5 seconds before next reading

if __name__ == "__main__":
    publish_motion()
