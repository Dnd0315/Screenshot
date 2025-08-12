import pyautogui
import datetime
import time
import os
import tkinter as tk

def take_screenshot(save_dir="screenshots"):
    # Create directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    # Generate filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(save_dir, filename)
    # Take screenshot
    #time.sleep(5)
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    screenshot.show()
    print(f"Screenshot saved to {filepath}")

root = tk.Tk()
root.title("Screenshot")
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, text="Take Screenshot", command=take_screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame, text="QUIT", command=root.quit)
close.pack(side=tk.LEFT)
root.mainloop()

