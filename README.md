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

## 📸 Hardware Prototype

Here is the physical implementation of SleepGuard AI, featuring the Raspberry Pi 4, camera, LCD screen, LED indicator, and buzzer.

![SleepGuard AI hardware prototype](Hardware%20integration.jpg)

*Figure 1: SleepGuard AI hardware prototype and its main components.*

## 🧪 Testing and Evaluation

### 💡 Lighting Condition Testing

Lighting condition testing is conducted indoors to evaluate the performance of the SleepGuard AI system under five different lighting conditions. The experiment examines how lighting affects facial landmark detection, Eye Aspect Ratio (EAR) readings, and the detection of prolonged eye closure.

### 🌤️ Experimental Conditions

1. ☀️ **Bright Lighting — Room Light**

   The room light is switched on to provide bright indoor illumination.

2. 🌞 **Normal Lighting — Sunlight**

   Natural sunlight is used as the primary source of illumination.

3. 💡 **Low Lighting — Table Lamp**

   A table lamp is used as the light source under reduced lighting conditions.

4. 🔦 **Very Low Lighting — Small Table Light**

   A small table light provides limited illumination to evaluate detection performance under very low lighting.

5. 🌑 **Dark Condition — Lights Off**

   The room lights and additional lights are switched off to examine whether the camera can still detect facial landmarks in darkness.

### 🎯 Testing Objectives

- 👁️ Evaluate facial landmark detection under different lighting conditions.
- 📊 Observe variations in EAR readings.
- ⏱️ Evaluate detection of prolonged eye closure.
- 🚨 Verify LED and buzzer activation when drowsiness is detected.
- 📲 Check whether Telegram notifications are delivered successfully.
- ⚠️ Identify detection failures or false alerts under different lighting conditions.

### 🔬 Testing Procedure

1. Position the camera and participant at a consistent distance.
2. Test the system under each of the five lighting conditions.
3. Observe the facial landmarks and EAR readings with eyes open and closed.
4. Keep the eye-closure duration consistent when testing the drowsiness alert.
5. Record whether the system detects the face and activates the LED, buzzer, and Telegram notification as expected.
6. Compare the observations across all five conditions.

### 📋 Results and Observations

The results will be recorded after testing is completed.

| No. | Lighting Condition | Face Detected | EAR Detection | Alert Activated | Remarks |
|---:|---|---|---|---|---|
| 1 | Bright — Room Light | Pending | Pending | Pending | — |
| 2 | Normal — Sunlight | Pending | Pending | Pending | — |
| 3 | Low — Table Lamp | Pending | Pending | Pending | — |
| 4 | Very Low — Small Table Light | Pending | Pending | Pending | — |
| 5 | Dark — Lights Off | Pending | Pending | Pending | — |

*Note: Results must be updated using actual experimental observations. Performance may vary with illumination, camera exposure, and facial landmark tracking quality.*

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

### 📱 Telegram Drowsiness Alert Notification

The SleepGuard AI system detects prolonged eye closure and sends a Telegram alert containing the EAR value, eye-closure duration, event number, timestamp, and LED and buzzer status.

![SleepGuard AI Telegram Alert](telegram_drowsiness_alert.png)

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
