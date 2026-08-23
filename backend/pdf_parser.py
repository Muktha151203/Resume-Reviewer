import pdfplumber


def extract_text_from_pdf(filepath):
    page_texts = []

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                page_texts.append(text)

    return "\n".join(page_texts).strip()