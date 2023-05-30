from pathlib import Path
from tkinter import *
from tkinter import filedialog, ttk

root = Tk()
root.title = "PDF Spliter"

btn_height = 1
btn_width = 10
btn_brd_width = 3
btn_padx = 1
btn_pady = 1

root.geometry("280x300")

pages_num = Entry(root)


# entry = Entry(root)
# entry.grid(column=0, row=2)
# entry.insert(0, "name")


def open_pdf_file():
    root.file_name = filedialog.askopenfilename(initialdir=Path(), title="Select *.pdf file",
                                                filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    pdf_file_label = Label(root, text="Selected document:", height=2)
    pdf_path_label = Label(root, text=Path(root.file_name).name, height=2, font='Helvetica 12 bold')
    pdf_file_label.pack()
    pdf_path_label.pack()

    ttk.Separator(root, orient="horizontal").pack(fill="x")

    pages_slicer_list()


def pdf_slicer_options():
    preview_pdf_btn = Button(root, text="Preview", command=pdf_preview, height=btn_height, width=btn_width,
                             borderwidth=btn_brd_width, pady=btn_pady, padx=btn_padx)
    split_pdf_btn = Button(root, text="Split!", command=pdf_split, height=btn_height, width=btn_width,
                           borderwidth=btn_brd_width, pady=btn_pady, padx=btn_padx)

    preview_pdf_btn.pack()
    split_pdf_btn.pack()


def pages_slicer_list():
    slice_pages_label = Label(root, text="Select pages where document\n must be cut (comma separate)", height=2)

    slice_pages_label.pack()
    pages_num.pack()

    pdf_slicer_options()


def pdf_preview():
    my_label = Label(root, text=pages_num.get())
    my_label.pack()


def pdf_split():
    my_label = Label(root, text=pages_num.get())
    my_label.pack()


# my_label = Label(root, text="Hello")
# my_label2 = Label(root, text="Ala ma kota")
# my_label3 = Label(root, text="Sierotka ma rysia")


open_pdf_btn = Button(root, text="Open PDF", command=open_pdf_file, height=btn_height, width=btn_width,
                      borderwidth=btn_brd_width)

open_pdf_btn.pack()

# my_label.grid(row=0, column=0)
# my_label2.grid(row=1, column=1)
# my_label3.grid(row=2, column=2)
# my_button.grid(row=3, column=0)

root.mainloop()
