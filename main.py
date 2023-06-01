from pathlib import Path
from tkinter import *
from tkinter import filedialog, ttk

from PdfSlicer.pdf_slicer import pdf_slicer_handler, show_new_pdf, read_pdf, get_modify_pages_slice_list

root = Tk()
root.title("PDF Spliter")

btn_height = 1
btn_width = 10
btn_brd_width = 3
btn_padx = 1
btn_pady = 1

root.geometry("280x300")

pdf_file_path = ""

main_frame = None


def open_pdf_file():
    global pdf_file_path, main_frame
    pdf_file_path = filedialog.askopenfilename(initialdir=Path(), title="Select *.pdf file",
                                               filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    if main_frame:
        main_frame.pack_forget()
    main_frame = LabelFrame(root, text='Slicer Options', borderwidth=10)
    main_frame.pack(pady=10)

    pages_num = Entry(main_frame)

    pdf_file_label = Label(main_frame, text="Selected document:", height=2)
    pdf_path_label = Label(main_frame, text=Path(pdf_file_path).name, height=2, font='Helvetica 12 bold')
    pdf_file_label.pack()
    pdf_path_label.pack()

    ttk.Separator(main_frame, orient="horizontal").pack(fill="x")

    pages_slicer_list(main_frame, pages_num)


def pdf_slicer_options(frame, pages_num):
    preview_pdf_btn = Button(frame, text="Preview", command=lambda: pdf_preview(frame, pages_num), height=btn_height,
                             width=btn_width, borderwidth=btn_brd_width, pady=btn_pady, padx=btn_padx)
    split_pdf_btn = Button(frame, text="Split!", command=lambda: pdf_split(frame, pages_num), height=btn_height,
                           width=btn_width, borderwidth=btn_brd_width, pady=btn_pady, padx=btn_padx)

    preview_pdf_btn.pack()
    split_pdf_btn.pack()


def pages_slicer_list(frame, pages_num):
    slice_pages_label = Label(frame, text="Select page(s) where document\n must be cut (comma separate)", height=2)
    slice_pages_label.pack()

    pages_num.pack()

    pdf_slicer_options(frame, pages_num)


def pdf_preview(frame, pages_num):
    if pages_num.get():
        pages_separator = [int(number) for number in pages_num.get().split(",")]
        metadata, pdf_content = read_pdf(Path(pdf_file_path))
        pages_list = get_modify_pages_slice_list(pages_separator, pdf_content)
        for index in range(len(pages_list) - 1):
            top_window = Toplevel()
            top_window.title(f"File {index}")

            pages = pdf_content[pages_list[index]:pages_list[index + 1]]

            new_window_size = f"{pages[0].mediabox.width}x{pages[0].mediabox.height}"
            top_window.geometry(new_window_size)

            scroll_bar = Scrollbar(top_window, orient=VERTICAL)

            pdf_file_to_txt = Text(top_window)
            pdf_file_to_txt.pack(fill=BOTH)
            scroll_bar.pack(side=RIGHT)

            pdf_text = ""
            for i, page in enumerate(pages):
                pdf_text += page.extract_text()
                pdf_text += "\n"
                pdf_text += f" Page {i} ".center(pages[0].mediabox.width//10, "-")
                pdf_text += "\n\n"
            pdf_file_to_txt.insert(1.0, pdf_text)
    else:
        Label(frame, text="Select page(s)", font="Helvetica 12 bold").pack()


def pdf_split(frame, pages_num):
    global pdf_file_path
    pages_separator = [int(number) for number in pages_num.get().split(",")]
    pdf_slicer_handler(Path(pdf_file_path), pages_separator, True)
    Label(frame, text="\nDone!", font="Helvetica 12 bold").pack()


open_pdf_btn = Button(root, text="Open PDF", command=open_pdf_file, height=btn_height, width=btn_width,
                      borderwidth=btn_brd_width)
open_pdf_btn.pack()

root.mainloop()
