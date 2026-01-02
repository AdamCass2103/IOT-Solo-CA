# iot-device/led_listener.py
import time
# from pubnub.pubnub import PubNub
# from pubnub.callbacks import SubscribeCallback
from config import LED_CHANNEL

def led_react(motion_detected):
    if motion_detected:
        print("LED ON (motion detected)")
    else:
        print("LED OFF (no motion)")

def listen_for_motion():
    """
    Simulate listening for motion events
    """
    motions = [True, False, True, False]  # Example sequence
    for motion in motions:
        led_react(motion)
        time.sleep(2)  # Wait 2 seconds between reactions

if __name__ == "__main__":
    listen_for_motion()
