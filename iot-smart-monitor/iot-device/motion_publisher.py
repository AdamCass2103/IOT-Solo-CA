# iot-device/motion_publisher.py

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from datetime import datetime
import time
import random
from config import PUBNUB_PUBLISH_KEY, PUBNUB_SUBSCRIBE_KEY, MOTION_CHANNEL

# Configure PubNub
pnconfig = PNConfiguration()
pnconfig.publish_key = PUBNUB_PUBLISH_KEY
pnconfig.subscribe_key = PUBNUB_SUBSCRIBE_KEY
pnconfig.uuid = "motion-sensor-001"
pubnub = PubNub(pnconfig)

def publish_motion(detected):
    message = {
        "detected": detected,
        "timestamp": str(datetime.utcnow())
    }
    pubnub.publish().channel(MOTION_CHANNEL).message(message).sync()
    print(f"Published: {message}")

if __name__ == "__main__":
    # Simulate motion every 5 seconds
    while True:
        detected = random.choice([True, False])
        publish_motion(detected)
        time.sleep(5)