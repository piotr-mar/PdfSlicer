from pathlib import Path

import click

from pdf_slicer import PdfSlicer


@click.command()
@click.argument("pdf_file", type=Path)
@click.option("-p", "--pages", type=str, required=True)
@click.option("-o", "--output_name", default=None, type=str,
              help='Output file name. Default "<pdf file name>_[pages-numbers]""')
@click.option("-d", "--output_dir", default=Path().absolute(), type=Path,
              help='Output file directory. Default current location')
def pdf_slicer_cli(pdf_file, pages, output_name, output_dir):
    if (not pdf_file.exists()
            and pdf_file.is_file
            and pdf_file.suffix == ".pdf"):
        raise FileNotFoundError(f"{pdf_file} not exist")

    if not output_name:
        output_name = pdf_file.name

    if not output_dir.exists() and output_dir.is_dir():
        raise FileNotFoundError(f"{output_dir} not exist")

    output = output_dir.joinpath(output_name)
    pdf_slicer = PdfSlicer(pdf_file, output, pages)
    pdf_slicer.split_pdf()


if __name__ == "__main__":
    pdf_slicer_cli()
