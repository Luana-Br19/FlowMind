from services.pdf_service import PDFService
from services.folder_service import FolderService


# pdf = PDFService()

# text = pdf.read(
#     "uploads/N8N_Rechnung.pdf"
# )


# print(text[:2000])

folder_service = FolderService()
tree = folder_service.get_tree()
print(tree)