# backend/pubnub_listener.py

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from models import db, MotionEvent
from config import PUBNUB_PUBLISH_KEY, PUBNUB_SUBSCRIBE_KEY, MOTION_CHANNEL
from flask import Flask

# Flask app context
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///motion.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# PubNub config
pnconfig = PNConfiguration()
pnconfig.publish_key = PUBNUB_PUBLISH_KEY
pnconfig.subscribe_key = PUBNUB_SUBSCRIBE_KEY
pnconfig.uuid = "backend-listener"
pubnub = PubNub(pnconfig)

class MotionListener(SubscribeCallback):
    def message(self, pubnub, message):
        data = message.message
        print(f"Received motion event: {data}")
        with app.app_context():
            event = MotionEvent(
                detected=data.get("detected", False)
            )
            db.session.add(event)
            db.session.commit()

pubnub.add_listener(MotionListener())
pubnub.subscribe().channels(MOTION_CHANNEL).execute()

print("Backend listening for motion events...")
