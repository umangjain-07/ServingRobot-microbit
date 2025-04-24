# 🤖 Smart Serving Robot | Micro:bit + MakeCode

An interactive, sensor-driven serving robot built using **Microsoft MakeCode** and **Micro:bit**, equipped with gesture, voice, and sensor-based controls. Designed for smart hospitality and automation scenarios.

## 📦 Project Overview

This robot combines intuitive controls with real-time responsiveness:

- **Motion Control** via button and tilt gestures
- **Voice Activation** for head movement
- **Tray Control** using tilt detection
- **Contactless Drawer System** powered by ultrasonic sensors
- **IR Gate System** that auto-opens on object detection for a few seconds

Developed with the [`RoboticsWorkshop`](https://github.com/gigotoys/RoboticsWorkShop) extension.

---

## 🧠 Features

- 🧭 **Navigation**  
  - `Button A` → Move Forward  
  - `Button B` → Move Backward  
  - `Button A + B` → Stop  
  - **Tilt Right** → Turn Right  
  - **Tilt Left** → Turn Left

- 🍽 **Tray Control**  
  - **Tilt Up** → Tray Up  
  - **Tilt Down** → Tray Down

- 🗣 **Head Movement**  
  - Triggered by **any voice/sound input**

- 📦 **Dual Drawers**  
  - **Ultrasonic sensor** detects hand presence  
  - Drawer auto-opens for a few seconds  
  - Fully contactless interaction

- 🚪 **IR Gate System**  
  - **IR sensor** detects objects  
  - Automatically opens the gate  
  - Closes after a few seconds (timed automation)

---

## 🔧 Setup Instructions

1. Open [Microsoft MakeCode](https://makecode.microbit.org/).
2. Import the extension:  
   `https://github.com/gigotoys/RoboticsWorkShop`
3. Add logic using blocks or Python as per control design.
4. Flash the code to your Micro:bit.
5. Connect your hardware (servo, IR sensor, ultrasonic sensor, etc.) accordingly.

---

## 👤 Author

**Umang Jain**  
Smart Robotics & Embedded Systems Enthusiast  
[GitHub](https://github.com/umangjain-07/) | [LinkedIn](https://www.linkedin.com/in/umangjain07/)

---

