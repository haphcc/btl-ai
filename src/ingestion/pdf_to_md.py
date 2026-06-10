from pathlib import Path
import sys

import fitz

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def remove_control_chars(text):
    allowed_controls = {"\n", "\r", "\t"}
    return "".join(
        char for char in text
        if char in allowed_controls or not char.iscontrol()
    )


def pdf_to_markdown(pdf_path, output_path):
    content = []

    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text("text")
            content.append(remove_control_chars(text))

    markdown_text = "\n\n".join(content)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(markdown_text, encoding="utf-8")


raw_dir = Path("data/raw")
processed_dir = Path("data/processed")

pdf_files = sorted(raw_dir.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError(f"Khong tim thay file PDF nao trong {raw_dir}")

for pdf_path in pdf_files:
    output_path = processed_dir / f"{pdf_path.stem}.md"
    pdf_to_markdown(pdf_path, output_path)
    print(f"Da chuyen: {pdf_path} -> {output_path}")

print("Hoan thanh!")
