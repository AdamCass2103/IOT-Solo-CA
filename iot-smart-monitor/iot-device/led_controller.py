# iot-device/led_listener.py

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from config import PUBNUB_PUBLISH_KEY, PUBNUB_SUBSCRIBE_KEY, LED_CHANNEL

# Configure PubNub
pnconfig = PNConfiguration()
pnconfig.publish_key = PUBNUB_PUBLISH_KEY
pnconfig.subscribe_key = PUBNUB_SUBSCRIBE_KEY
pnconfig.uuid = "led-listener-001"
pubnub = PubNub(pnconfig)

class LEDListener(SubscribeCallback):
    def message(self, pubnub, message):
        print(f"LED Command Received: {message.message}")
        # Here you can add GPIO code later to control an LED

pubnub.add_listener(LEDListener())
pubnub.subscribe().channels(LED_CHANNEL).execute()

print("Listening for LED commands...")
