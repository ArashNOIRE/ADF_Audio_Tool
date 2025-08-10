# GTA Vice City MP3 ↔ ADF Converter

A simple Python tool with a minimal GUI to convert between `.mp3` and `.adf` audio formats used by **GTA: Vice City** radio stations.

## ✨ Features
- Convert **MP3 → ADF** and **ADF → MP3**
- Minimal and user-friendly GUI (Tkinter)
- Works without Python installed after building with PyInstaller
- Cross-platform builds for Windows, Linux

---

##  Project Structure
├── converter.py # Main script with GUI
├── requirements.txt # Additional dependencies if any
├── build_windows.sh # Docker-based Windows build script
├── build_linux.sh # Docker-based Linux build script
├── build_macos.sh # Native macOS build script
├── README.md # This file
├── .gitignore # Ignored files/folders
└── dist/ # Output binaries (ignored)

---

## 🔧 Usage

### 1. Running from Python
```bash
python converter.py
```

### 2. Building Executables
- Windows (.exe) from any OS:
```bash
  bash build_windows.sh
```
- Linux binary from any OS:
```bash
  bash build_linux.sh
```

- Compiled output will be in the ```dist/``` directory.

---

## 🖥 Requirements
- Python 3.8+ (for running from source)

- PyInstaller (for building executables)

- Docker (for cross-platform builds on Linux/Windows)

---

## 📜 License
This project is released under the MIT License.
You are free to use, modify, and distribute it for any purpose.

---

## 💡 Notes
```.adf``` files in GTA Vice City are simply MP3 files XOR-encoded with 0x22.

This tool does not contain any copyrighted game files.

You can use it to replace or restore your own GTA Vice City radio tracks.

