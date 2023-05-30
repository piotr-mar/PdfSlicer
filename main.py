from pathlib import Path
from tkinter import *
from tkinter import filedialog, ttk

root = Tk()
root.title = "PDF Spliter"
btn_height = 2
btn_width = 10
btn_brd_width = 3
root.geometry("280x300")
# entry = Entry(root)
# entry.grid(column=0, row=2)
# entry.insert(0, "name")


def open_pdf_file():
    root.file_name = filedialog.askopenfilename(initialdir=Path(), title="Select *.pdf file",
                                                filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf_file_label = Label(root, text="Selected document:", height=2)
    pdf_path_label = Label(root, text=Path(root.file_name).name, height=2)
    pdf_file_label.pack()
    pdf_path_label.pack()

    ttk.Separator(root, orient="horizontal").pack(fill="x")


def pdf_slicer_options():
    preview_pdf_btn = Button(root, text="Preview", command=pdf_preview, height=btn_height, width=btn_width,
                             borderwidth=btn_brd_width)
    split_pdf_btn = Button(root, text="Split!", command=pdf_split, height=btn_height, width=btn_width,
                           borderwidth=btn_brd_width)
    pdf_path_label = Label(root, text=Path(root.file_name).name, height=2)

    preview_pdf_btn.pack()
    split_pdf_btn.pack()


def pdf_preview():
    pass


def pdf_split():
    pass


# my_label = Label(root, text="Hello")
# my_label2 = Label(root, text="Ala ma kota")
# my_label3 = Label(root, text="Sierotka ma rysia")


open_pdf_btn = Button(root, text="Open PDF", command=open_pdf_file, height=btn_height, width=btn_width, borderwidth=btn_brd_width)


open_pdf_btn.pack()



# my_label.grid(row=0, column=0)
# my_label2.grid(row=1, column=1)
# my_label3.grid(row=2, column=2)
# my_button.grid(row=3, column=0)

root.mainloop()
