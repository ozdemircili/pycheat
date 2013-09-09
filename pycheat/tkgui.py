import Tkinter
import tkMessageBox
#tkMessageBox.showinfo(title="Greetings", message="Hello World!")
top = Tkinter.Tk()

def helloCallBack():
    tkMessageBox.showinfo("Hello","Hey there!")

B = Tkinter.Button(top, text="Hello", command = helloCallBack)

B.pack()
top.mainloop()
