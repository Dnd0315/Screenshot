import pyautogui
import datetime
import os

def take_screenshot(save_dir="screenshots"):
    # Create directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    # Generate filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(save_dir, filename)
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"Screenshot saved to {filepath}")

if __name__ == "__main__":
    take_screenshot()