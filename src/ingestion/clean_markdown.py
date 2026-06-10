import re
from pathlib import Path
from collections import Counter

def remove_repeated_headers_footers(text):
    lines = text.split('\n')
    if len(lines) < 3:
        return text
    
    header_candidates = []
    for i in range(min(5, len(lines))):
        if lines[i].strip():
            header_candidates.append(lines[i])
    
    first_10_lines = lines[:min(10, len(lines))]
    line_counts = Counter(first_10_lines)
    repeated_header = None
    for line, count in line_counts.items():
        if count >= 2 and line.strip():
            repeated_header = line
            break
    
    if repeated_header:
        cleaned_lines = []
        first_occurrence = True
        for line in lines:
            if line == repeated_header:
                if first_occurrence:
                    cleaned_lines.append(line)
                    first_occurrence = False
            else:
                cleaned_lines.append(line)
        lines = cleaned_lines
    
    last_10_lines = lines[-min(10, len(lines)):]
    line_counts_footer = Counter(last_10_lines)
    repeated_footer = None
    for line, count in line_counts_footer.items():
        if count >= 2 and line.strip() and line != repeated_header:
            repeated_footer = line
            break
    
    if repeated_footer:
        cleaned_lines = []
        last_occurrence_idx = -1
        for idx, line in enumerate(lines):
            if line == repeated_footer:
                last_occurrence_idx = idx
            cleaned_lines.append(line)
        
        final_lines = []
        for idx, line in enumerate(cleaned_lines):
            if line == repeated_footer and idx < last_occurrence_idx:
                continue
            final_lines.append(line)
        lines = final_lines
    
    return '\n'.join(lines)

def clean_markdown(text):
    text = re.sub(r"Trang\s+\d+", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = remove_repeated_headers_footers(text)
    
    return text.strip()

input_dir = Path("data/mdfile")
output_dir = Path("data/afterclean")
output_dir.mkdir(parents=True, exist_ok=True)

for input_file in sorted(input_dir.glob("*.md")):
    text = input_file.read_text(encoding="utf-8")
    cleaned = clean_markdown(text)
    output_file = output_dir / input_file.name
    output_file.write_text(cleaned, encoding="utf-8")
    print(f"Đã làm sạch: {input_file.name} -> {output_file}")

print("Hoàn tất làm sạch tất cả file markdown.")