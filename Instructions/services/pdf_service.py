import fitz
import pytesseract
from pathlib import Path
from pdf2image import convert_from_path
from services.llm_service import LLMService


class PDFService:

    def read(self, file_path: str) -> str:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Datei nicht gefunden: {file_path}"
            )

        # 1. Versuch: normalen PDF-Text lesen
        text = self.extract_text(path)

        # 2. Wenn kein Text vorhanden -> OCR
        if not text.strip():
            print("Kein Textlayer gefunden -> OCR")
            text = self.extract_ocr(file_path)

        print(text)
        return text


    def extract_text(self, path):

        text = ""
        document = fitz.open(path)

        for page in document:

            text += page.get_text()

        document.close()
        return text

    def extract_ocr(self, path):

        text = ""
        pages = convert_from_path(
            path,
            dpi=300
        )

        for page in pages:

            text += pytesseract.image_to_string(
                page,
                lang="deu"
            )

        return text

    def attachment_reader(self, intake):
        if intake.input_type in ["pdf", "xlsx", "md"]:
            pdf_path = intake.attachments[0]

            return self.read(
                pdf_path
            )
        else:
            print(f"Dokumententyp {intake.input_type} nicht lesbar")
            return