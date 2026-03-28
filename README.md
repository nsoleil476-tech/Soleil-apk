# Mister-Flasheur IA Player 🎵

Mister-Flasheur IA Player is a modern music playback application developed with Python, Kivy, and KivyMD. It is designed to provide a smooth user experience with a dark interface and AI-assisted features.

## 🚀 Features
* **Dark Interface**: An elegant design optimized for visual comfort.
* **Automatic Scan**: Automatically searches for MP3 files in your device's Music folder.
* **Advanced Control**: Play, pause, skip tracks, and interactive progress bar.
* **AI Options (In Progress)**: Dedicated buttons for voice commands and hum-to-search functionality.
* **Tab Management**: Organization by Artists, Albums, and Playlists.

## 🛠️ Installation & Configuration
The application is configured to be compiled for Android via **Buildozer**.

### Prerequisites
* Python 3
* Kivy (v2.2.1)
* KivyMD (v1.1.1)

### Android Compilation
To generate the APK file, use the following command in your Linux/Pydroid environment:
```bash
buildozer android debug
📱 Required Permissions
To function correctly on a smartphone, the app requests access to:
External Storage (to read MP3 files).
Microphone (for future AI features).
Developed by Mister-Flasheur / Dj Emmato  
