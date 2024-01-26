import pyautogui
import time
import random
import sys

pyautogui.FAILSAFE = False

def switch() -> None:
    """
    Switches the active screen using Alt + Tab
    a random number of times.
    """
    max_switches = random.randint(1, 5)
    pyautogui.keyDown('alt') 
    
    for _ in range(1, max_switches):
        pyautogui.press('tab')     
     
    pyautogui.keyUp('alt')   

def wiggle() -> None:
    """
    Wiggles the mouse between two coordinates.
    """
    max_wiggles = random.randint(4, 9)
    
    for _ in range(1, max_wiggles):
        coords = get_rand_coords()
        pyautogui.moveTo(
            x=coords[0], 
            y=coords[1],
            duration=5
        )
        time.sleep(350)
    

def get_rand_coords() -> []:
    """
    Returns a list of coordinates in the 
    format [x=1980, y=1080]
    """
    screen = pyautogui.size()
    width = screen[0]
    height = screen[1]
    
    return [
        random.randint(100, width - 200),
        random.randint(100, height - 200)
    ]


if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    try:
        while True:
            switch()
            wiggle()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")
