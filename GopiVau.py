import tkinter as RashiBen
    
def write_slogan():
    print("Main thi, Tum thi, Kon Tha..... KON THAAA?")
    
def write_slogan1():
    print("Yeh Rashi.. Cooker me se chane nikaal liye or khali cooker gas pe chadha diya :/")
    
    
root = RashiBen.Tk()
frame = RashiBen.Frame(root)
frame.pack()

button = RashiBen.Button(frame , text="X" , fg="red" , command=quit)


button.pack(side=RashiBen.LEFT)
slogan = RashiBen.Button(frame , text="Rasode kon tha ?" , command=write_slogan)
slogan.pack(side=RashiBen.LEFT)

                   
button.pack(side=RashiBen.RIGHT)
slogan = RashiBen.Button(frame , text="Rashi Ben" , command=write_slogan1)
slogan.pack(side=RashiBen.RIGHT)

root.mainloop()