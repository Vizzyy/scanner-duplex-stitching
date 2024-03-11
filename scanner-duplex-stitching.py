#! python3

from PyPDF2 import PdfWriter, PdfReader
import sys

output_pdf = PdfWriter()

if (len(sys.argv)) != 3:
    print(f'Wrong number of arguments. First argument is input path, and the second argument is output path.')
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

print(f'Input path: {input_file_path}')
print(f'Output path: {output_file_path}')

with open(input_file_path, 'rb') as readfile:
    input_pdf = PdfReader(readfile)

    print(f'Pages found: {len(input_pdf.pages)}')

    pairs = int(len(input_pdf.pages)/2)

    if (pairs % 2) != 0:
        print(f'Exiting due to an odd number of pages.')
        sys.exit(1)

    ptr = 0
    while ptr < pairs:
        first_pair_idx = ptr
        second_pair_idx = (len(input_pdf.pages) - 1) - ptr
        # print(f'pairs: {pairs}, ptr: {ptr}, first_pair_idx: {first_pair_idx}, second_pair_idx: {second_pair_idx}')
        output_pdf.add_page(input_pdf.pages[first_pair_idx])
        output_pdf.add_page(input_pdf.pages[second_pair_idx])
        ptr += 1

    with open(output_file_path, "wb") as writefile:
        output_pdf.write(writefile)

print('Done!')
