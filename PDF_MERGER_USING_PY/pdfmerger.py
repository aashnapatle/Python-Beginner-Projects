from  PyPDF2 import PdfWriter
merger = PdfWriter()

pdfs=[]
n = int(input("Enter the number of pdfs you want to merge: "))
for i in range(0,n):
    name=input(f"Enter the name of pdf {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append("PDF_MERGER_USING_PY/" + pdf)
merger.write("PDF_MERGER_USING_PY/merged.pdf")
merger.close()