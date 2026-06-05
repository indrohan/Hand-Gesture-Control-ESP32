# Hand Gesture Controlled ESP32 LED System

## Overview

This project uses Computer Vision and Embedded Systems to control LEDs connected to an ESP32 using hand gestures detected through a webcam.

The Python application uses OpenCV and MediaPipe to detect hand gestures, then sends commands to the ESP32 over Wi-Fi using the HTTP protocol.

## Features

* Real-time hand gesture detection
* ESP32 Wi-Fi communication
* Control 4 LEDs using gestures
* HTTP Client-Server architecture
* Computer Vision + IoT integration

## Hardware Used

* ESP32 Development Board
* 4 LEDs
* 220Ω Resistors
* USB Cable
* Laptop Webcam

## Software Used

* Python
* OpenCV
* MediaPipe
* Requests
* Arduino IDE

## Gesture Mapping

| Gesture   | Action       |
| --------- | ------------ |
| 1 Finger  | LED1 ON      |
| 2 Fingers | LED2 ON      |
| 3 Fingers | LED3 ON      |
| 4 Fingers | LED4 ON      |
| Fist      | All LEDs OFF |

## Communication Protocol

HTTP Protocol over Wi-Fi

## Technologies

* Embedded Systems
* ESP32
* IoT
* Computer Vision
* Python
* Arduino

## Author

Nishant Kiran Ghorpade
B.Tech Electronics & Telecommunication Engineering
