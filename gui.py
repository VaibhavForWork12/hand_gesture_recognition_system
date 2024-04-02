import tkinter as tk
from subprocess import call,Popen
import threading

pyprog = 'hand_gesture_detection.py'

def callpy():
    process = Popen(['python', '-i', pyprog] )
    return process
    print("process Id",process.pid)

process = callpy()
def quitpy():
    process.terminate()
root = tk.Tk()

#getting screen width and height of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#setting tkinter root size
root.geometry("%dx%d" % (width/2, height))
root.title("Hand Gesture Recognition")

# creating text label to display on root screen
label = tk.Label(root, text="REAL-TIME HAND GESTURE RECOGNITION", font=("Arial", 22))
label.pack()
 
tk.Button(root, text='Start' , font=("Arial", 15) ,bg = 'blue', command=threading.Thread(target=callpy).start).pack()
# print("Call Pid :" , Popen.pid)

tk.Button(root, text="Close window",font=("Arial", 15) , bg = 'yellow',  command = root.destroy).pack()
tk.Button(root, text="Terminate Recogniser",font=("Arial", 15),bg = 'red',  command = quitpy ).pack()

root.mainloop()



# btn = Button(root, text="Click Me", command=threading.Thread(target=callpy).st