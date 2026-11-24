from pypdf import PdfReader, PdfWriter

reader = PdfReader("AccountStatement_19112026_183315_unlocked (5).pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Copy existing metadata and update creation/modification timestamps
metadata = dict(reader.metadata or {})
pdf_timestamp = "D:20261119145055Z"
metadata["/CreationDate"] = pdf_timestamp
metadata["/ModDate"] = pdf_timestamp

writer.add_metadata(metadata)

with open("AccountStatement_19112026_183315_updated.pdf", "wb") as f:
    writer.write(f)