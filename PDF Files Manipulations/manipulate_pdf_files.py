# Author = 'Eda Aydın'

"""
Outcomes of this project are
1) Extract information from a pdf
2) Copy a single page and put it in a newly created pdf
3) Rotate pdfs and write them to a new pdf
4) Read multiple pages
5) Adding Watermark to pdf
"""

"""
- Please install PyPDF2 which is a common python library to work with PDF files. 
- The library can be used to read text from PDF files.
- You can install the library as follows: pip install PyPDF2 
"""

# 1 Extract Information From a PDF.

from PyPDF2 import PdfFileReader, PdfFileWriter


# Reading binary format for pdf file
f = open("Harvard_Business_School.pdf", "rb")
read_pdf = PdfFileReader(f)
get_documentation_info = read_pdf.getDocumentInfo()
print(get_documentation_info)

page_number = read_pdf.numPages
print(page_number)

page5 = read_pdf.getPage(5).extractText()
print(page5)

page6 = read_pdf.getPage(6).extractText()
print(page6)

f.close()

# 2 Copy a Single Page and Put it a newly created PDF.

f2 = open("Harvard_Business_School.pdf", "rb")
read_pdf2 = PdfFileReader(f2)
sample_page2 = read_pdf.getPage(4)

write_pdf2 = PdfFileWriter()
write_pdf2.addPage(sample_page2)
# After reading the sample_page2, the new page will be added.

pdf_output2 = open("Sample_PDF_File.pdf", "wb")
write_pdf2.write(pdf_output2)

f2.close()
pdf_output2.close()

# 3 Extract Page 5 and sample_pdf_file2.pdf

f3 = open("Harvard_Business_School.pdf","rb")
read_pdf3 = PdfFileReader(f3)
sample_page3 = read_pdf3.getPage(5)

write_pdf3 = PdfFileWriter()
write_pdf3.addPage(sample_page3)

pdf_output3 = open("Sample_PDF_File_2.pdf","wb")
write_pdf3.write(pdf_output3)

f3.close()
pdf_output3.close()

# 4 Rotate PDFs and Write Them to a new pdf.
f4 = open("Harvard_Business_School.pdf", "rb")
read_pdf4 = PdfFileReader(f4)
write_pdf4 = PdfFileWriter()

rotated_page = read_pdf4.getPage(2).rotateClockwise(90)
write_pdf4.addPage(rotated_page)

pdf_output4 = open("Sample_PDF_Rotated.pdf","wb")
write_pdf4.write(pdf_output4)

f4.close()
pdf_output4.close()


# 5 Read Multiple Pages.
f5 = open("Harvard_Business_School.pdf", "rb")
read_pdf5 = PdfFileReader(f5)

num_page = read_pdf5.numPages

pdf_text_all =[]
for page in range(num_page):
    one_page_text = read_pdf5.getPage(page).extractText()
    pdf_text_all.append(one_page_text)

print(len(pdf_text_all))


# Exercise
f_exercise = open("Harvard_Business_School.pdf","rb")
read_pdf_exercise = PdfFileReader(f_exercise)

num_page_exercise = 4

pdf_text_all_exercise = []

for page in range(num_page_exercise):
    one_page_text_exercise = read_pdf_exercise.getPage(page).extractText()
    pdf_text_all_exercise.append(one_page_text_exercise)


# 6 Adding Watermark to PDF.

f6 = open("watermark_conf_2.pdf", 'rb')
read_watermark = PdfFileReader(f6)

watermark_page = read_watermark.getPage(0)

f7 = open("Harvard_Business_School.pdf", "rb")
read_pdf7 = PdfFileReader(f7)

write_pdf7 = PdfFileWriter()

num_pages = read_pdf7.getNumPages()

for page in range(num_pages):
    # Get the page from second pdf document
    single_page = read_pdf7.getPage(page)
    # Merge page from second pdf document and watermark page
    single_page.mergePage(watermark_page)
    # add Page
    write_pdf7.addPage(single_page)

pdf_output7 = open("Sample_PDF_watermarked.pdf","wb")
# write the watermarked file to the new file
write_pdf7.write(pdf_output7)

f6.close()
f7.close()
pdf_output7.close()

