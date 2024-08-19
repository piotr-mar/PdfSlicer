from dataclasses import dataclass
from typing import List

from PyPDF2 import PdfReader, PdfWriter, DocumentInformation


@dataclass
class PdfData:
    metadata: DocumentInformation
    pages_data: List


class PdfSlicer:
    def __init__(self, pdf_file, output, pages_slice):
        self.output = output
        self.pdf_data = self.read_pdf(pdf_file)
        self.pages_slice = self.get_pages_slice_list(pages_slice)

    @staticmethod
    def read_pdf(pdf_file):
        reader = PdfReader(pdf_file)
        pdf_data = PdfData(reader.metadata, reader.pages)
        return pdf_data

    def get_pages_slice_list(self, slices):
        slices = slices.replace(" ", "").split(",")
        try:
            slices.insert(0, 0)
            slices.append(len(self.pdf_data.pages_data))
            slices = [int(number) for number in slices]
            return slices
        except ValueError as err:
            raise ValueError('Pages must be numbers')

    def save_new_pdf(self, pages, pages_range):
        file_name = f"{self.output.stem}_{pages_range}.pdf"

        writer = PdfWriter()
        for page in pages:
            writer.add_page(page)

        writer.add_metadata(self.pdf_data.metadata)

        with open(file_name, "wb") as pdf_file:
            writer.write(pdf_file)

    def split_pdf(self):
        for index in range(len(self.pages_slice) - 1):
            pages = pdf_pages[self.pages_slice[index]:self.pages_slice[index + 1]]
            pages_range = f"{self.pages_slice[index]}-{self.pages_slice[index + 1]}"
            self.save_new_pdf(pages, pages_range)


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


def pdf_handler(page_sliced_list, metadata, save_pdf=False):
    for index in range(len(page_slice_list) - 1):
        pages = pdf_pages[page_sliced_list[index]:page_sliced_list[index + 1]]
        pages_range = f"{page_sliced_list[index]}-{page_sliced_list[index + 1]}"

        if save_pdf:
            save_new_pdf(pages, pages_range, metadata)
        else:
            show_new_pdf()


def show_new_pdf():
    pass


path_to_pdf_file = "Umowa-Giganci.pdf"
pages_slice_list = [1]

metadata, pdf_pages = read_pdf(path_to_pdf_file)

page_slice_list = get_modify_pages_slice_list(pages_slice_list, pdf_pages)

pdf_handler(page_slice_list, metadata, True)
