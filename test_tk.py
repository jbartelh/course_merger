from Tkinter import *
from tkFileDialog   import askopenfilename      

def callback():
    name= askopenfilename() 
    print name
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(padx=30, pady=5)

Button(text='File Open', command=callback).pack(padx=30, pady=5)

mainloop()