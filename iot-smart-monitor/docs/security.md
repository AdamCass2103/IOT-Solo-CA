# Security Considerations

## IoT Device Access
- Devices will use encrypted communication with PubNub.
- Devices require authentication keys.

## PubNub Channels
- Publish and subscribe channels are secured with PubNub keys.
- Only registered devices can publish messages.

## Database Security
- Database access requires strong password.
- Use SQLAlchemy ORM to prevent SQL injection.
- Data at rest will be encrypted if using MySQL in production.

## Webserver Security
- Flask app will run behind HTTPS (SSL certificate from Let's Encrypt).
- API endpoints will require authentication tokens in production.

## Data in Transit
- All communication between devices and server uses secure PubNub channels.
- Webserver uses HTTPS to protect user data.
