# GTA Vice City MP3 ↔ ADF Converter

A simple Python tool with a minimal GUI to convert between `.mp3` and `.adf` audio formats used by **GTA: Vice City** radio stations.

## ✨ Features
- Convert **MP3 → ADF** and **ADF → MP3**
- Minimal and user-friendly GUI (Tkinter)
- Works without Python installed after building with PyInstaller

---

## 🔧 Usage

### 1. Running from Python
```bash
  python converter.py
```
Or
```bash
  python3 converter.py
```

### 2. Building Executables
- **On Windows and Linux and MacOS:**
```bash
  pyinstaller --onefile --noconsole --icon=icon.ico converter.py
```

- Compiled output will be in the ```dist/``` directory.

---

## 🖥 Requirements
- Python 3.8+ (for running from source)

- PyInstaller (for building executables)

---

## 📜 License
This project is released under the MIT License.
You are free to use, modify, and distribute it for any purpose.

---

## 💡 Notes
```.adf``` files in GTA Vice City are simply MP3 files XOR-encoded with 0x22.

This tool does not contain any copyrighted game files.

You can use it to replace or restore your own GTA Vice City radio tracks.

---

## Source
[GTAMods](https://gtamods.com/wiki/ADF)
