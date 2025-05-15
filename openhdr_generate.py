import cv2
import os
import json
import numpy as np
import argparse

def compute_brightness(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return np.mean(hsv[:, :, 2])

def detect_scenes(video_path, threshold=15.0):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    scene_data = []

    last_brightness = None
    current_scene = {
        "start": 0,
        "brightness": 1.0,
        "contrast": 1.0,
        "saturation": 1.0
    }

    frame_index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        time_sec = frame_index / fps
        brightness = compute_brightness(frame)

        if last_brightness is not None:
            delta = abs(brightness - last_brightness)
            if delta > threshold:
                current_scene["end"] = round(time_sec, 2)
                scene_data.append(current_scene.copy())
                current_scene = {
                    "start": round(time_sec, 2),
                    "brightness": round(brightness / 128, 2),
                    "contrast": 1.0,
                    "saturation": 1.0
                }

        last_brightness = brightness
        frame_index += 1
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    current_scene["end"] = round(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps, 2)
    scene_data.append(current_scene)

    cap.release()
    return scene_data

def save_metadata(video_path, scenes):
    name = os.path.basename(video_path)
    output = {
        "version": "2.0",
        "video": name,
        "metadata_type": "scene_auto",
        "scenes": scenes
    }

    os.makedirs("metadata", exist_ok=True)
    out_path = os.path.join("metadata", name + ".hdrmeta.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=4)

    print(f"[✓] Metadata saved to {out_path}")

def main():
    print("Please enter mpv with the selected video")
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="Input video path")
    args = parser.parse_args()

    scenes = detect_scenes(args.video)
    save_metadata(args.video, scenes)
    
if __name__ == "__main__":
    main()
