import joblib
import os
import numpy as np

def extract_features(file_path):
    try:
        size = os.path.getsize(file_path)
        with open(file_path, "rb") as f:
            content = f.read()
            entropy = -sum(p * np.log2(p) for p in np.bincount(bytearray(content), minlength=256) / len(content) if p > 0)
        return [size, entropy]
    except:
        return [0, 0]

def scan_with_ml(file_path):
    model = joblib.load("models/malware_detector.pkl")
    features = extract_features(file_path)
    prediction = model.predict([features])[0]
    return "⚠ Malware Detected!" if prediction == 1 else "✅ File is Safe."
