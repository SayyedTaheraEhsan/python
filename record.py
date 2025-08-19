import cv2
import numpy as np
import pyautogui

# Output file name
output = "screen_record.avi"

# Screen resolution
screen_size = pyautogui.size()

# Define video writer (XVID codec, 20 fps)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output, fourcc, 20.0, screen_size)

print("🎥 Recording... Press Ctrl+C to stop.")

try:
    while True:
        # Take screenshot
        img = pyautogui.screenshot()
        
        # Convert to array
        frame = np.array(img)
        
        # Convert RGB -> BGR (OpenCV format)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Write frame
        out.write(frame)
except KeyboardInterrupt:
    print("\n🛑 Recording stopped.")

out.release()
cv2.destroyAllWindows()
