import pypdf
import sys

pdf_path = r'd:\Agents\portfolio\Portfolio\Resume\Roshan_resume_BA.pdf'
out_path = r'd:\Agents\portfolio\portfolio\resume_extracted.txt'

try:
    reader = pypdf.PdfReader(pdf_path)
    text = '\n'.join([page.extract_text() for page in reader.pages])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Extraction successful.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
