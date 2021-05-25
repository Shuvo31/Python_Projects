import time
import pyautogui
import tkinter as tk
def screenshot():
    n=int(round(time.time()*1000))
    n="{}.png".format(n)
    img=pyautogui.screenshot(n)
    img.show()
r=tk.Tk()
frame=tk.Frame(r)
frame.pack()
button=tk.Button(frame,text="Take screenshot",command=screenshot)
button.pack(side=tk.LEFT)
close=tk.Button(frame,text="QUIT",command=quit)
close.pack(side=tk.LEFT)
r.mainloop()