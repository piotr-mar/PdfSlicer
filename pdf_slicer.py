from PyPDF2 import PdfReader, PdfWriter


def read_pdf(path_to_pdf):
    reader = PdfReader(path_to_pdf)
    return reader.metadata, reader.pages


def save_new_pdf(split_pages, pages_range, metadata):
    writer = PdfWriter()

    for page in split_pages:
        writer.add_page(page)

    writer.add_metadata(metadata)
    file_name = f"{metadata.title}_{pages_range}.pdf"

    with open(file_name, "wb") as pdf_file:
        writer.write(pdf_file)


def get_modify_pages_slice_list(slice_list_to_change, pages):
    slice_list_to_change.insert(0, 0)
    slice_list_to_change.append(len(pages))
    return slice_list_to_change


def pdf_handler(page_sliced_list, pdf_pages, metadata, save_pdf=False):
    for index in range(len(page_sliced_list) - 1):
        pages = pdf_pages[page_sliced_list[index]:page_sliced_list[index + 1]]
        pages_range = f"{page_sliced_list[index]}-{page_sliced_list[index + 1]}"

        if save_pdf:
            save_new_pdf(pages, pages_range, metadata)
        else:
            show_new_pdf()


def show_new_pdf():
    pass


def pdf_slicer_handler(path_to_pdf_file, pages_list, save=False):
    metadata, pdf_pages = read_pdf(path_to_pdf_file)

    page_slice_list = get_modify_pages_slice_list(pages_list, pdf_pages)

    pdf_handler(page_slice_list, pdf_pages, metadata, save)
