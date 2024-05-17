from pykeyboard import PyKeyboard

import time
import pyperclip 
import tkinter as tk

kboard = PyKeyboard()

root = tk.Tk()
root.title("1Word_1Line")

label = tk.Label(root, text="Please Input below:")
label.pack(pady=10)

entry = tk.Entry(root, width=45)
entry.pack(pady=10)

def on_button_click():

    time.sleep(3)
    input_text = entry.get()  

    for i in range(len(input_text)):
        time.sleep(0.1)
        pyperclip.copy(input_text[i])
        #以下语句模拟键盘点击ctrl+v
        kboard.press_key(kboard.control_key)
        kboard.tap_key('v')
        kboard.release_key(kboard.control_key)

        kboard.tap_key(kboard.enter_key)

button = tk.Button(root, text="Auto output in 3 seconds", command=on_button_click)
button.pack(pady=5)


root.mainloop()
