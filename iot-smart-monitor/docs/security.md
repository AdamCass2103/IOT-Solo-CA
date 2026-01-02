# Security Plan

## IoT Device
- Device access protected with strong passwords
- SSH key authentication for Raspberry Pi
- No hardcoded keys in code

## PubNub
- Channels secured with publish/subscribe keys
- Avoid exposing keys publicly
- Use token-based access in production

## Database
- Use strong passwords for MySQL
- Store hashed passwords (bcrypt) for users
- Limit access to backend only

## Webserver / HTTPS
- Apache or Nginx with WSGI
- Redirect HTTP → HTTPS
- Enable firewall to allow only required ports
