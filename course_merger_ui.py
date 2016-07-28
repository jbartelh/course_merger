from tkinter import Tk, Label, Button
from tkFileDialog   import askopenfilename
import course_merger as cm

class App:
    
    availabletypes = [("exported edX-course", ("*.tar.gz"))]
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.firstfile = None
        self.secondfile = None

        self.firstfile_button = Button(master, text="Pick 1st course", command=self.choose_first_file, width=16)
        self.firstfile_button.grid(row=1, column=0, padx=5, pady=5)
        self.firstfile_label = Label(master)
        self.firstfile_label.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        
        self.secondfile_button = Button(master, text="Pick 2nd course", command=self.choose_second_file, width=16)
        self.secondfile_button.grid(row=2, column=0, padx=5, pady=5)
        self.secondfile_label = Label(master)
        self.secondfile_label.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        
        self.merge_button = Button(master, text="Merge courses", command=self.merge, width=16)
        self.merge_button.grid(row=3, column=2, padx=5, pady=5, sticky='E')

    def choose_first_file(self):
        self.firstfile = askopenfilename(filetypes=App.availabletypes)
        self.firstfile_label['text'] = self.firstfile
        
    def choose_second_file(self):
        self.secondfile = askopenfilename(filetypes=App.availabletypes)
        self.secondfile_label['text'] = self.secondfile
        
    def merge(self):
        print self.firstfile, self.secondfile
        cm.merge_course(self.firstfile, self.secondfile)
        self.firstfile = None
        self.firstfile_label['text'] = ''
        self.secondfile = None
        self.secondfile_label['text'] = ''

def main():
    ''' main '''
    root = Tk()
    root.resizable(width=False, height=False)
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
