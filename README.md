# IOT-Solo-CA
# IoT Motion Monitor

## Overview
This project is a smart motion monitoring system using IoT sensors and LED indicators. Motion events are sent from IoT devices to a cloud server using PubNub and stored in a database. The web frontend displays live motion events and history. 

## Project Structure
- `backend/` : Flask backend, database models, PubNub listener
- `frontend/` : HTML templates and CSS for the web app
- `iot-device/` : Simulated IoT devices (motion sensors & LED control)
- `docs/` : Architecture diagram, hardware Fritzing sketch, security documentation

## Running Locally
1. Clone this repository.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate


