import pygetwindow as gw
from pywinauto.application import Application

def minimize_windows(title):
    # Find all windows that include the title
    all_windows = gw.getWindowsWithTitle(title)
    
    for window in all_windows:
        # For each window, use its handle with pywinauto to minimize
        try:
            app = Application().connect(handle=window._hWnd)
            app_window = app.window(handle=window._hWnd)
            app_window.minimize()
            print(f"Minimized: {window.title}")
        except Exception as e:
            print(f"Could not minimize {window.title}: {e}")

# Minimize all windows containing 'pyth.exe' in their title
minimize_windows('pyth.exe')
