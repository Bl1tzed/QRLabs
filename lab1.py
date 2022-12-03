from pywinauto import Application
import time
app = Application().start(cmd_line=r"C:\Program Files\PuTTY\putty.exe")
time.sleep(2)
app = Application().connect(title="PuTTY Configuration")
window = app.PuTTYConfigBox
window.set_focus()
window[u"Host Name (or IP address):Edit"].type_keys("sdf.org")
window["Open"].click()
time.sleep(2)
putty = app.PuTTY
putty.type_keys("blitzed")
putty.type_keys("{ENTER}")
time.sleep(1)
putty.type_keys("8fmn0yadAQtmZQ")
putty.type_keys("{ENTER}")
putty.type_keys("{BACKSPACE}")
time.sleep(5)
