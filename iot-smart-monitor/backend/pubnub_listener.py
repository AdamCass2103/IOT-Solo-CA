# backend/pubnub_listener.py
from config import PUBNUB_SUBSCRIBE_KEY, MOTION_CHANNEL

def handle_motion_event(message):
    """
    This function will handle motion messages from PubNub
    Currently, just prints the message
    """
    print("Received motion message:", message)

def subscribe_to_channel():
    """
    Placeholder for PubNub subscription
    """
    print(f"Would subscribe to channel: {MOTION_CHANNEL} with key {PUBNUB_SUBSCRIBE_KEY}")

if __name__ == "__main__":
    subscribe_to_channel()
    # Later: use PubNub SDK to actually subscribe and call handle_motion_event on new messages
