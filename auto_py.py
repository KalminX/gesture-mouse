import pyautogui
import time

# Get screen size
width, height = pyautogui.size()
print(f"Screen size: {width}x{height}")

# Move to center of the screen
center_x, center_y = width // 2, height // 2
print("Moving mouse to center of screen...")
pyautogui.moveTo(center_x, center_y, duration=1)

# Click at the center
print("Clicking...")
pyautogui.click()

# Type some text
print("Typing a message...")
pyautogui.write('FLybae!!!\nAbeg help me cook spaghetti... Hunger dey kpai me!', interval=0.3)

# Take a screenshot
print("Taking screenshot...")
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')
print("Screenshot saved as screenshot.png")

# Done
print("Done!")

