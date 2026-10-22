# 🚘 SleepGuard AI

### 🧠 AI-Based Driver Drowsiness Detection System with IoT Alert Mechanism for Lorry Drivers

<p align="center">
  <strong>👁️ Detect Eye Closure · 🚨 Trigger Alerts · 📲 Notify Remotely</strong>
</p>

---

## 🌟 About the Project

**SleepGuard AI** is an AI-powered driver drowsiness detection prototype designed to help identify signs of drowsiness in lorry drivers through real-time eye monitoring.

Built around a **Raspberry Pi 4**, the system uses computer vision to analyse facial landmarks and calculate the **Eye Aspect Ratio (EAR)**. When prolonged eye closure is detected, an LED and buzzer provide local warnings, while a Telegram notification delivers a remote alert.

🎯 **Our mission:** To explore how AI, embedded systems, and IoT technology can work together to support driver awareness and road safety.

## ✨ Key Features

- 👁️ **Real-Time Eye Monitoring** — Tracks facial landmarks using MediaPipe Face Mesh.
- 🧮 **EAR-Based Detection** — Calculates the Eye Aspect Ratio to identify eye closure.
- ⏱️ **Duration Monitoring** — Detects prolonged eye closure using a configurable time threshold.
- 💡 **LED Warning** — Activates a visual warning when a drowsiness event is detected.
- 🔊 **Buzzer Alarm** — Provides an audible local alert.
- 📲 **Telegram Notifications** — Sends remote alerts with detection information.
- 📊 **Live Monitoring Display** — Shows EAR values, eye status, and alert information.

## ⚙️ How It Works

```text
📷 Camera Input
      ↓
🧠 Facial Landmark Detection
      ↓
🧮 Calculate Eye Aspect Ratio (EAR)
      ↓
👁️ Check Eye Closure
      ↓
⏱️ Monitor Closure Duration
      ↓
🚨 Drowsiness Event Detected
      ↓
💡 LED + 🔊 Buzzer + 📲 Telegram Alert
```

## 🛠️ Hardware Components

| Component | Purpose |
|---|---|
| 🖥️ Raspberry Pi 4 | Main processing unit |
| 📷 Camera module | Captures the driver's face |
| 🖥️ 7-inch HDMI display | Displays the monitoring interface |
| 💡 LED | Visual warning indicator |
| 🔊 Buzzer | Audible warning alarm |
| 🔌 Power supply and wiring | Powers and connects the system |

## 💻 Software & Technologies

- 🐍 **Python** — Main programming language
- 👁️ **OpenCV** — Image processing and display
- 🧠 **MediaPipe Face Mesh** — Facial landmark detection
- 📸 **Picamera2** — Raspberry Pi camera interface
- ⚡ **GPIO Zero** — LED and buzzer control
- 🌐 **Telegram Bot API** — Remote alert delivery
- 📡 **Requests** — HTTP communication with Telegram

## 🧮 Detection Configuration

| Parameter | Current Setting |
|---|---|
| Eye Aspect Ratio threshold | `0.21` |
| Eye-closure duration | `2.0 seconds` |
| Camera resolution | `640 × 480` |
| LED GPIO pin | `GPIO 21` |
| Buzzer GPIO pin | `GPIO 16` |

*These are the current prototype settings. Calibration and further testing may be required for different users, lighting conditions, and camera positions.*

## 📸 Project Demonstration

Screenshots and demonstration images will be added here as the project documentation is prepared.

- 📷 Live camera monitoring interface
- 🚨 Drowsiness detection and local alarm activation
- 📲 Telegram alert notification

## 🚧 Current Development Status

**Implemented and tested on the prototype:**

- ✅ Camera-based facial landmark detection
- ✅ EAR calculation and eye-closure monitoring
- ✅ Prolonged eye-closure alert logic
- ✅ LED and buzzer activation
- ✅ Telegram drowsiness notifications

**Potential future enhancements:**

- 🔍 Mouth Aspect Ratio (MAR) and yawning detection
- 🧭 Head-pose estimation
- 📈 More extensive testing and performance evaluation
- ⚙️ Calibration for different lighting and operating conditions

> **Note:** MAR, yawning detection, and head-pose detection are future enhancements, not current implemented features.

## 🔐 Security

- Never publish Telegram bot tokens or passwords.
- Store credentials outside the source code.
- Exclude secret configuration files using `.gitignore`.
- Keep private credentials out of screenshots and documentation.

## ⚠️ Disclaimer

SleepGuard AI is an academic prototype developed for learning, demonstration, and evaluation. It is not a certified automotive safety system and must not replace driver responsibility, adequate rest, or established road-safety procedures.

## 🎓 Project Purpose

This project explores the integration of **Artificial Intelligence, Computer Vision, Embedded Systems, and the Internet of Things (IoT)** in a practical driver-monitoring application.

---

<p align="center">
  🚘 <strong>SleepGuard AI</strong><br>
  <em>Smarter Monitoring. Earlier Warnings. Safer Journeys.</em>
</p>
