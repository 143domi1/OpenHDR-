# OpenHDR++


# OpenHDR++  
**A free, open, smart dynamic HDR metadata system for Linux and open-source video players.**

> Inspired by Dolby Vision, built for freedom.

---

## What is OpenHDR++?

OpenHDR++ is a lightweight, modular system for bringing **dynamic HDR metadata** to Linux-based players like **MPV** — allowing **per-scene brightness, contrast, and saturation adjustments** in real time.

Whether you're watching SDR or HDR10 content, OpenHDR++ lets you create a better, more immersive viewing experience **without proprietary tech**.



## Features

- ✅ Real-time scene-aware metadata switching via MPV script  
- ✅ Python tool to **automatically detect scenes** and generate `.json` metadata  
- ✅ Easy-to-edit JSON files for full customization  
- ✅ FOSS (Free and open source)
- ✅ Works with any standard video (MP4, MKV, etc.)


## Project Structure

openhdr/ ├── metadata/                # Stores auto-generated or manual scene metadata │   └── yourvideo.mp4.hdrmeta.json ├── player/ │   └── mpv_openscript.lua  # MPV Lua script for dynamic scene adjustment ├── tools/ │   └── openhdr_generate.py # Python tool for automatic metadata generation ├── README.md └── LICENSE


## Installation

### 1. Install requirements

    pip install opencv-python numpy

2. Link the MPV Lua script

Edit or create ~/.config/mpv/scripts/ and copy the Lua script:

    mkdir -p ~/.config/mpv/scripts
    cp player/mpv_openscript.lua ~/.config/mpv/scripts/



Usage

Step 1: Generate Metadata

    cd tools
    python openhdr_generate.py ../yourvideo.mp4

This creates a .hdrmeta.json file in the metadata/ folder.

Step 2: Play the video with MPV

    mpv ../yourvideo.mp4

MPV will read the metadata and apply real-time enhancements.



Metadata Format (JSON)

    {
      "version": "2.0",
      "video": "yourvideo.mp4",
      "metadata_type": "scene_auto",
      "scenes": [
        {
          "start": 0.0,
          "end": 8.4,
          "brightness": 1.1,
          "contrast": 1.0,
          "saturation": 1.1
        }
      ]
    }

You can edit this manually or use the Python tool to regenerate.



License

This project is licensed under the MIT License — see LICENSE for details.
You are free to use, modify, and distribute it.



Goals for Future Versions

GUI for editing HDR scene metadata

AI-powered scene detection using PySceneDetect or deep learning

FFmpeg integration for encoded output

Support for HDR10+ sidecar metadata

Real-time tone mapping previews


## Diffrence between **SDR** and **OpenHDR++**
**SDR**
![Screenshot From 2025-05-14 09-23-47](https://github.com/user-attachments/assets/6c447dd8-d250-4284-865f-33b8a974e4a4)

**OpenHDR++**

![Screenshot From 2025-05-14 09-23-08](https://github.com/user-attachments/assets/6780cd6a-65d4-44e0-b893-45954b7a93b8)


## Contributing
Pull requests are welcome!
If you want to help with GPU acceleration, GUI design, or AI integration — open an issue or message the creator.

