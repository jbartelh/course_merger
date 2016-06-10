import Tkinter as tk
import ttk
import xml.etree.ElementTree as etree


class App(tk.Frame):
    ''' GUI-Application Class '''

    def __init__(self, master, filename):

        tk.Frame.__init__(self, master)
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text=filename, anchor='w')

        self.xml_tree = etree.parse(filename)
        self.xml_root = self.xml_tree.getroot()


        root_node = self.tree.insert('', 'end', text=self.xml_root.tag, open=True)
        self.__process_directory(root_node, self.xml_root)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        self.grid()

    def __process_directory(self, parent, element):
        ''' Adds xml-Elements recursive to the TreeView '''

        for child in element:
            oid = self.tree.insert(parent, 'end', text=child.tag, open=False)

            self.__process_directory(oid, child)

def main():
    ''' main '''
    root = tk.Tk()
    app = App(root, filename='./tmp/2016_SS/course.xml')
    app.mainloop()

if __name__ == '__main__':
    main()
