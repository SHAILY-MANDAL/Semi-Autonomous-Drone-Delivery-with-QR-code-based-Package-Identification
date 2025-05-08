# Semi-Autonomous-Drone-Delivery-with-QR-code-based-Package-Identification
🚁 Autonomous Drone Delivery System with QR Code Precision
An intelligent drone delivery system designed for autonomous navigation, package identification, and real-time decision-making. This project integrates QR code detection using a Raspberry Pi camera, allowing drones to precisely identify and pick up packages without human intervention.

🔍 Core Features:

Autonomous Navigation – Follows pre-programmed GPS paths using Mission Planner.
QR Code Detection – Uses Raspberry Pi camera to scan and identify packages.
Precise Hovering – Detects QR code from a fixed height for accurate pickup.
Obstacle Handling – Designed to navigate complex environments.
Payload Capacity – Can lift up to 1500 grams over a range of 1 km.
🔧 Hardware Components:

Raspberry Pi 4 + PiCamera v1.3
Brushless Motors (A2212) + 30A ESCs
GPS Module
5200mAh Li-Po Battery
Drone Frame, Flight Controller, Propellers
📦 Software Stack:

Python (QR detection)
OpenCV (image processing)
Mission Planner (for flight path setup and monitoring)
ArduPilot firmware for autonomous control
