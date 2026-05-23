from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    from src.core.config import config
except ModuleNotFoundError:
    from core.config import config


PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CHUNKS_DIR = PROJECT_ROOT / "data" / "chunks"
CHUNKS_PATH = CHUNKS_DIR / "chunks.jsonl"
CHUNK_REPORT_PATH = CHUNKS_DIR / "chunk_report.json"

TARGET_TOKENS = int(config.CHUNK_SIZE or 900)
OVERLAP_TOKENS = int(config.CHUNK_OVERLAP or 120)
HARD_MAX_TOKENS = 1200
MIN_CHUNK_TOKENS = 120

PAGE_COMMENT_RE = re.compile(r"^\s*<!--\s*page\s+\d+\s*-->\s*$", re.I)
TRANG_MARKER_RE = re.compile(r"^\s*#{0,6}\s*(TRANG|PAGE)\s+\d+\s*$", re.I)
ISOLATED_PAGE_NO_RE = re.compile(r"^\s*\d{1,3}\s*$")
DATE_FOOTER_RE = re.compile(r"^\s*\d{1,2}/\d{1,2}/\d{4}\s+.{0,60}\s+\d{1,3}\s*$")
FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
CHAPTER_RE = re.compile(r"(?:chuong|chương|chapter|lecture|bai|bài|c|ch)[_\s-]*(\d{1,2}(?:[.,]\d)?)", re.I)
ARTICLE_RE = re.compile(r"^(#{1,6}\s*)?(Điều|Äiá»u)\s+\d+[\.:]", re.I)

NOISE_LINE_PATTERNS = [
    re.compile(r"^\s*BANKING ACADEMY OF VIETNAM\s*$", re.I),
    re.compile(r"^\s*HỌC VIỆN NGÂN HÀNG\s*$", re.I),
    re.compile(r"^\s*HOC VIEN NGAN HANG\s*$", re.I),
    re.compile(r"^\s*ITDE\s*$", re.I),
    re.compile(r"^\s*INFORMATION TECHNOLOGY\s*&?\s*DIGITAL ECONOMICS\s*$", re.I),
    re.compile(r"^\s*KHOA\s+(CÔNG NGHỆ THÔNG TIN|HỆ THỐNG THÔNG TIN|HTTT|Công nghệ thông tin).*$", re.I),
    re.compile(r"^\s*Khoa Hệ thống thông tin quản lý\s+[-–]\s+Học viện Ngân Hàng\s*$", re.I),
    re.compile(r"^\s*ORACLE\s*$", re.I),
]

MOJIBAKE_TOKENS = ("Ä ", "Ä)", "Æ", "â€", "�")

COMMON_TEXT_REPLACEMENTS = {
    "Cácứng dụng": "Các ứng dụng",
    "Tap mục": "Tập mục",
    "tap mục": "tập mục",
    "tập mụcứng": "tập mục ứng",
    "mụcứng": "mục ứng",
    "phổbi ến": "phổ biến",
    "tất cảcác": "tất cả các",
    "khuy ến nghịtr ực": "khuyến nghị trực",
    "Tu vấn": "Tư vấn",
    "khách hang": "khách hàng",
    "Dw liệu": "Dữ liệu",
    "Kho khăn": "Khó khăn",
    "dộ&gt;": "độ",
    "độkh ó": "độ khó",
    "độh ỗtr ợ": "độ hỗ trợ",
    "hỗtr ợcho": "hỗ trợ cho",
    "ho trợra": "hỗ trợ ra",
    "có thểquan": "có thể quan",
    "bán lẻ(": "bán lẻ (",
    "Từtập": "Từ tập",
    "độdo": "độ đo",
    "dễhi ểu": "dễ hiểu",
    "dễđ ánh": "dễ đánh",
    "nghi êm": "nghiêm",
    "va tin": "và tin",
    "rời ra c hoá": "rời rạc hóa",
    "rời dịch vụ": "rời bỏ dịch vụ",
    "Minh„ họa thuậta toán7 Apriori5. (2)": "Minh họa thuật toán Apriori",
    "Sinh tap cac": "Sinh tập các",
    "ứng vien": "ứng viên",
    "điểm chữnhư": "điểm chữ như",
    "đưới đây": "dưới đây",
    "trừcác": "trừ các",
    "Điểm theo chir thang 4": "Điểm theo chữ thang 4",
    "cụthểtrong": "cụ thể trong",
    "học phầntiên": "học phần tiên",
    "quy chếcủa": "quy chế của",
}

OCR_JUNK_MARKERS = (
    "r N ˆ~",
    "Prescriptive Analytics dối)",
    "= Diagnostic la Analytics",
    "= Diagnostic hơi Analytics",
    "‹ x S v",
    'z `" ® z ^ z',
)


@dataclass
class AuditResult:
    file_count: int
    issue_counts: Counter
    by_dir: dict[str, Counter]
    flagged_files: list[dict]


def rel_path(path: Path) -> str:
    return path.relative_to(PROJECT_ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def token_estimate(text: str) -> int:
    # A conservative mixed Vietnamese/code estimate without adding tokenizer deps.
    words = re.findall(r"\w+|[^\s\w]", text, flags=re.UNICODE)
    return max(1, int(len(words) * 0.75))


def sha16(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def normalize_for_compare(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]+", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def is_probably_auto_title(line: str, file_stem: str) -> bool:
    match = HEADING_RE.match(line.strip())
    if not match:
        return False
    title = match.group(2).strip()
    normalized_title = normalize_for_compare(title)
    normalized_stem = normalize_for_compare(file_stem)
    if normalized_title == normalized_stem:
        return True
    if re.fullmatch(r"(?:\d+)?ch\d{1,2}(?:\s*[-_]\s*20\d{2})?", normalized_title, re.I):
        return True
    if re.fullmatch(r"[0-9a-f]{8}.*", title, re.I):
        return True
    if re.fullmatch(r"\d{1,2}", title):
        return True
    return False


def is_noise_line(line: str, repeated_count: int) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if any(pattern.match(stripped) for pattern in NOISE_LINE_PATTERNS):
        return True
    if repeated_count >= 3 and re.match(r"^\s*#{1,6}\s*(HỌC VIỆN|BANKING ACADEMY|ITDE)\b", stripped, re.I):
        return True
    if repeated_count >= 4 and len(stripped) <= 90:
        if re.search(r"(BANKING ACADEMY|HỌC VIỆN|KHOA|ITDE|ORACLE DATABASE)", stripped, re.I):
            return True
    return False


def is_short_date_footer(line: str) -> bool:
    stripped = line.strip()
    if stripped.startswith("|"):
        return False
    return bool(DATE_FOOTER_RE.match(stripped))


def protected_line_counts(lines: list[str]) -> Counter:
    counts: Counter = Counter()
    in_code = False
    for line in lines:
        if FENCE_RE.match(line):
            in_code = not in_code
            continue
        stripped = line.strip()
        if stripped:
            counts[stripped] += 1
    return counts


def is_structural_markdown_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith(("#", ">", "```", "---", "***", "___")):
        return True
    if stripped.startswith(("- ", "* ", "+ ", "[ ] ", "[x] ", "[X] ")):
        return True
    if re.match(r"^\s*(?:\d+|[A-Za-z])[\.)/]\s+", stripped):
        return True
    if "|" in stripped:
        return True
    return False


def looks_like_code_or_formula_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith(("`", "$", "=>", "->", "←", "→")):
        return True
    if stripped.endswith(("`", "$", "{", "}", ";")):
        return True
    if stripped.count("$") >= 2 or stripped.count("`") >= 2:
        return True
    code_tokens = ("SELECT ", "FROM ", "WHERE ", "INSERT ", "UPDATE ", "DELETE ", "CREATE ", "ALTER ", "BEGIN", "END", "DECLARE")
    if any(token in stripped.upper() for token in code_tokens):
        return True
    if re.search(r"[{}=<>]{2,}|\\\\(?:pmod|mod|rightarrow|Rightarrow|Leftrightarrow)", stripped):
        return True
    return False


def should_unwrap_with_next(line: str, next_line: str) -> bool:
    stripped = line.strip()
    nxt = next_line.strip()
    if is_structural_markdown_line(stripped) or is_structural_markdown_line(nxt):
        return False
    if looks_like_code_or_formula_line(stripped) or looks_like_code_or_formula_line(nxt):
        return False
    if len(stripped) < 35 or len(nxt) < 12:
        return False
    if re.search(r"[.!?:;。)\]}]$", stripped):
        return False
    first = nxt[0]
    if first.isdigit() or first == first.lower() or stripped.endswith(","):
        return True
    return False


def unwrap_soft_line_breaks(lines: list[str]) -> list[str]:
    unwrapped: list[str] = []
    paragraph = ""
    in_code = False

    for index, line in enumerate(lines):
        if FENCE_RE.match(line):
            if paragraph:
                unwrapped.append(paragraph.rstrip())
                paragraph = ""
            in_code = not in_code
            unwrapped.append(line.rstrip())
            continue
        if in_code:
            unwrapped.append(line.rstrip())
            continue

        stripped = line.strip()
        if not stripped:
            if paragraph:
                unwrapped.append(paragraph.rstrip())
                paragraph = ""
            if unwrapped and unwrapped[-1] != "":
                unwrapped.append("")
            continue

        current = paragraph if paragraph else line.rstrip()
        next_line = lines[index + 1] if index + 1 < len(lines) else ""
        if should_unwrap_with_next(current, next_line):
            paragraph = f"{current.rstrip()} {next_line.strip()}"
            continue

        if paragraph:
            unwrapped.append(paragraph.rstrip())
            paragraph = ""
        else:
            unwrapped.append(line.rstrip())

    if paragraph:
        unwrapped.append(paragraph.rstrip())
    return unwrapped


def clean_markdown_text(text: str, file_path: Path) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\ufeff", "")
    for old, new in COMMON_TEXT_REPLACEMENTS.items():
        text = text.replace(old, new)
    lines = text.split("\n")
    counts = protected_line_counts(lines)
    cleaned: list[str] = []
    in_code = False
    first_content_seen = False
    seen_duplicate_headings: set[str] = set()

    for line in lines:
        stripped = line.strip()
        if FENCE_RE.match(line):
            in_code = not in_code
            cleaned.append(line.rstrip())
            first_content_seen = True
            continue
        if in_code:
            cleaned.append(line.rstrip())
            continue

        if not first_content_seen and not stripped:
            continue
        if not first_content_seen and is_probably_auto_title(line, file_path.stem):
            continue
        if any(marker in stripped for marker in OCR_JUNK_MARKERS):
            continue
        if stripped.startswith("a ^ “:A (3)"):
            continue
        if stripped.startswith("Sex: female; Age: from 25 to 35"):
            line = "Sex: female; Age: 25-35; Marital status: married; Condition: having baby"
            stripped = line
        if "top=1" in stripped and "&nbsp;" in stripped:
            line = "top=1 / top=0"
            stripped = line
        if stripped.startswith("|. "):
            line = "## " + stripped[3:].strip()
            stripped = line
        if stripped in {"- Tp | k |. 0 -", "°K."}:
            continue
        if PAGE_COMMENT_RE.match(stripped) or TRANG_MARKER_RE.match(stripped):
            continue
        if ISOLATED_PAGE_NO_RE.match(stripped):
            continue
        if is_short_date_footer(stripped):
            continue
        if is_noise_line(stripped, counts[stripped]):
            continue
        if re.match(r"^\s*[-–—]{3,}\s*$", stripped) and counts[stripped] >= 8:
            continue

        heading = HEADING_RE.match(stripped)
        if heading:
            heading_key = normalize_for_compare(heading.group(2))
            if counts[stripped] >= 4 and heading_key in seen_duplicate_headings:
                continue
            seen_duplicate_headings.add(heading_key)

        cleaned.append(line.rstrip())
        if stripped:
            first_content_seen = True

    cleaned = unwrap_soft_line_breaks(cleaned)
    result = "\n".join(cleaned)
    result = re.sub(r"\n{3,}", "\n\n", result).strip() + "\n"
    return result


def audit_file(path: Path) -> dict:
    text = read_text(path)
    lines = text.splitlines()
    issue_counts = Counter()
    in_code = False
    for line in lines:
        if FENCE_RE.match(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        stripped = line.strip()
        issue_counts["page_comment"] += int(bool(PAGE_COMMENT_RE.match(stripped)))
        issue_counts["trang_marker"] += int(bool(TRANG_MARKER_RE.match(stripped)))
        issue_counts["isolated_page_no"] += int(bool(ISOLATED_PAGE_NO_RE.match(stripped)))
        issue_counts["date_slide_footer"] += int(is_short_date_footer(line))
    issue_counts["mojibake_suspect"] = sum(text.count(token) for token in MOJIBAKE_TOKENS)
    nonempty = [line.strip() for line in lines if line.strip()]
    repeated = Counter(nonempty)
    repeated_noise = [
        {"line": line, "count": count}
        for line, count in repeated.items()
        if count >= 3 and is_noise_line(line, count)
    ]
    issue_counts["repeated_noise"] = len(repeated_noise)
    if lines:
        first = next((line for line in lines if line.strip()), "")
        issue_counts["auto_title"] = int(is_probably_auto_title(first, path.stem))
    return {
        "path": rel_path(path),
        "line_count": len(lines),
        "char_count": len(text),
        "heading_count": sum(1 for line in lines if HEADING_RE.match(line.strip())),
        "issues": {key: value for key, value in issue_counts.items() if value},
        "repeated_noise_examples": repeated_noise[:5],
    }


def audit(processed_dir: Path = PROCESSED_DIR) -> AuditResult:
    files = sorted(processed_dir.rglob("*.md"))
    totals: Counter = Counter()
    by_dir: dict[str, Counter] = defaultdict(Counter)
    flagged: list[dict] = []
    for path in files:
        item = audit_file(path)
        issues = item["issues"]
        if issues:
            flagged.append(item)
        for key, value in issues.items():
            totals[key] += value
            by_dir[path.parent.name][key] += value
    return AuditResult(len(files), totals, dict(by_dir), flagged)


def print_audit(result: AuditResult) -> None:
    print(f"MD files: {result.file_count}")
    print("Issue counts:")
    for key, value in result.issue_counts.most_common():
        print(f"  {key}: {value}")
    print("Top directories:")
    for directory, counts in sorted(result.by_dir.items(), key=lambda item: sum(item[1].values()), reverse=True)[:25]:
        print(f"  {directory}: {dict(counts)}")
    print(f"Flagged files: {len(result.flagged_files)}")
    for item in result.flagged_files[:30]:
        print(f"  {item['path']}: {item['issues']}")


def clean(processed_dir: Path = PROCESSED_DIR) -> dict:
    changed = 0
    unchanged = 0
    for path in sorted(processed_dir.rglob("*.md")):
        original = read_text(path)
        cleaned = clean_markdown_text(original, path)
        if cleaned != original:
            write_text(path, cleaned)
            changed += 1
        else:
            unchanged += 1
    return {"changed": changed, "unchanged": unchanged}


def infer_doc_type(path: Path, title: str) -> str:
    lower = f"{path.as_posix()} {title}".lower()
    if "quydinhquyche" in lower or re.search(r"\b(qd|nq|thong tu|quy che|quy dinh)\b", lower):
        if "tuyen sinh" in lower:
            return "admission"
        return "regulation"
    if "de cuong" in lower or "giới thiệu môn học" in lower or "gioi thieu mon hoc" in lower:
        return "syllabus"
    return "course_material"


def infer_title(path: Path, text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("!"):
            continue
        heading = HEADING_RE.match(stripped)
        if heading:
            return heading.group(2).strip(" *")
        if len(stripped) > 8:
            return stripped.strip(" *")
    return path.stem


def infer_chapter(path: Path, title: str, text: str) -> tuple[str | None, str | None]:
    source = " ".join([path.stem, title, "\n".join(text.splitlines()[:20])])
    match = CHAPTER_RE.search(source)
    chapter_no = match.group(1).replace(",", ".") if match else None
    chapter_title = None
    for line in text.splitlines()[:30]:
        heading = HEADING_RE.match(line.strip())
        if heading and re.search(r"(CHƯƠNG|CHUONG|CHAPTER|LECTURE|BÀI|BAI)", heading.group(2), re.I):
            chapter_title = heading.group(2).strip()
            continue
        if chapter_title and heading:
            chapter_title = f"{chapter_title} - {heading.group(2).strip()}"
            break
    if not chapter_title and chapter_no:
        chapter_title = title
    return chapter_no, chapter_title


def subject_name(subject_dir: str) -> str:
    names = {
        "QuyDinhQuyCheHVNH": "Quy định, quy chế HVNH",
        "tkcsdl": "Thiết kế cơ sở dữ liệu",
        "csdl": "Cơ sở dữ liệu",
        "hqtcsdl": "Hệ quản trị cơ sở dữ liệu",
        "ATBMTT": "An toàn bảo mật thông tin",
    }
    return names.get(subject_dir, subject_dir.replace("_", " "))


def iter_blocks(text: str) -> Iterable[tuple[str, int, int, list[str]]]:
    lines = text.splitlines(keepends=True)
    headings: list[tuple[int, str]] = []
    buffer: list[str] = []
    start = 0
    pos = 0
    in_code = False

    def current_path() -> list[str]:
        return [title for _, title in headings]

    for line in lines:
        line_start = pos
        pos += len(line)
        if FENCE_RE.match(line):
            in_code = not in_code
        heading = None if in_code else HEADING_RE.match(line.strip())
        article = None if in_code else ARTICLE_RE.match(line.strip())
        is_boundary = bool(heading or article)
        if is_boundary and buffer:
            block_text = "".join(buffer).strip()
            if block_text:
                yield block_text, start, line_start, current_path()
            buffer = []
            start = line_start
        if heading:
            level = len(heading.group(1))
            title = heading.group(2).strip()
            headings = [(lvl, txt) for lvl, txt in headings if lvl < level]
            headings.append((level, title))
        buffer.append(line)
    if buffer:
        block_text = "".join(buffer).strip()
        if block_text:
            yield block_text, start, len(text), current_path()


def split_large_block(block: str, max_tokens: int = TARGET_TOKENS) -> list[str]:
    if token_estimate(block) <= max_tokens:
        return [block]
    units = re.split(r"(\n\s*\n)", block)
    paragraphs: list[str] = []
    current = ""
    for unit in units:
        current += unit
        if unit.strip() == "":
            if current.strip():
                paragraphs.append(current.strip())
            current = ""
    if current.strip():
        paragraphs.append(current.strip())
    if not paragraphs:
        paragraphs = block.splitlines()

    chunks: list[str] = []
    current_parts: list[str] = []
    for para in paragraphs:
        candidate = "\n\n".join(current_parts + [para]).strip()
        if current_parts and token_estimate(candidate) > max_tokens:
            chunks.append("\n\n".join(current_parts).strip())
            if token_estimate(para) > max_tokens:
                chunks.extend(split_oversized_text(para, max_tokens))
                current_parts = []
            else:
                current_parts = [para]
        elif token_estimate(para) > max_tokens:
            for piece in split_oversized_text(para, max_tokens):
                chunks.append(piece)
            current_parts = []
        else:
            current_parts.append(para)
    if current_parts:
        chunks.append("\n\n".join(current_parts).strip())
    return [chunk for chunk in chunks if chunk]


def split_oversized_text(text: str, max_tokens: int = HARD_MAX_TOKENS) -> list[str]:
    pieces: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        candidate = "\n".join(current + [line]).strip()
        if current and token_estimate(candidate) > max_tokens:
            pieces.append("\n".join(current).strip())
            current = [line]
        elif token_estimate(line) > max_tokens:
            if current:
                pieces.append("\n".join(current).strip())
                current = []
            pieces.extend(split_long_line(line, max_tokens))
        else:
            current.append(line)
    if current:
        pieces.append("\n".join(current).strip())
    return [piece for piece in pieces if piece]


def split_long_line(line: str, max_tokens: int = HARD_MAX_TOKENS) -> list[str]:
    tokens = re.findall(r"\w+|[^\s\w]", line, flags=re.UNICODE)
    if not tokens:
        return [line]
    max_raw_tokens = max(50, int(max_tokens / 0.75))
    return [" ".join(tokens[i : i + max_raw_tokens]).strip() for i in range(0, len(tokens), max_raw_tokens)]


def with_overlap(previous: str, current: str, overlap_tokens: int = OVERLAP_TOKENS) -> str:
    if not previous or overlap_tokens <= 0:
        return current
    words = previous.split()
    overlap_words = max(1, int(overlap_tokens / 0.75))
    prefix = " ".join(words[-overlap_words:])
    if not prefix:
        return current
    candidate = f"{prefix}\n\n{current}"
    if token_estimate(candidate) > HARD_MAX_TOKENS:
        return current
    return candidate


def chunk_file(path: Path, created_at: str) -> list[dict]:
    text = read_text(path)
    source_hash = sha16(text)
    title = infer_title(path, text)
    doc_type = infer_doc_type(path, title)
    chapter_no, chapter_title = infer_chapter(path, title, text)
    subject_dir = path.parent.name
    blocks = list(iter_blocks(text))

    chunks: list[dict] = []
    current = ""
    current_start = 0
    current_end = 0
    current_section: list[str] = []
    previous_text = ""

    def flush() -> None:
        nonlocal current, current_start, current_end, current_section, previous_text
        content = current.strip()
        if not content:
            return
        if chunks:
            content = with_overlap(previous_text, content)
        content_hash = sha16(content)
        chunk_index = len(chunks)
        chunks.append(
            {
                "chunk_id": sha16(f"{rel_path(path)}:{chunk_index}:{content_hash}"),
                "text": content,
                "source_path": rel_path(path),
                "source_file": path.name,
                "subject_dir": subject_dir,
                "subject_name": subject_name(subject_dir),
                "document_title": title,
                "doc_type": doc_type,
                "chapter_no": chapter_no,
                "chapter_title": chapter_title,
                "section_path": current_section,
                "chunk_index": chunk_index,
                "char_start": current_start,
                "char_end": current_end,
                "token_estimate": token_estimate(content),
                "content_hash": content_hash,
                "source_hash": source_hash,
                "created_at": created_at,
            }
        )
        previous_text = content
        current = ""
        current_start = 0
        current_end = 0
        current_section = []

    for block, start, end, section_path in blocks:
        for part in split_large_block(block):
            candidate = f"{current}\n\n{part}".strip() if current else part
            if current and token_estimate(candidate) > HARD_MAX_TOKENS:
                flush()
            elif current and token_estimate(candidate) > TARGET_TOKENS and token_estimate(current) >= MIN_CHUNK_TOKENS:
                flush()
            if not current:
                current_start = start
                current_section = section_path
            current = f"{current}\n\n{part}".strip() if current else part
            current_end = end
            if token_estimate(current) >= HARD_MAX_TOKENS:
                flush()
    flush()
    return chunks


def write_chunks(processed_dir: Path = PROCESSED_DIR, chunks_path: Path = CHUNKS_PATH) -> dict:
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    created_at = datetime.now(timezone.utc).isoformat()
    all_chunks: list[dict] = []
    per_file: dict[str, int] = {}
    for path in sorted(processed_dir.rglob("*.md")):
        chunks = chunk_file(path, created_at)
        all_chunks.extend(chunks)
        per_file[rel_path(path)] = len(chunks)

    with chunks_path.open("w", encoding="utf-8", newline="\n") as handle:
        for chunk in all_chunks:
            handle.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    token_counts = [chunk["token_estimate"] for chunk in all_chunks]
    report = {
        "created_at": created_at,
        "source_file_count": len(per_file),
        "chunk_count": len(all_chunks),
        "output_path": rel_path(chunks_path),
        "min_tokens": min(token_counts) if token_counts else 0,
        "max_tokens": max(token_counts) if token_counts else 0,
        "avg_tokens": round(sum(token_counts) / len(token_counts), 2) if token_counts else 0,
        "chunks_over_hard_max": sum(1 for count in token_counts if count > HARD_MAX_TOKENS),
        "files_without_chunks": [path for path, count in per_file.items() if count == 0],
        "chunks_per_file": per_file,
    }
    write_text(CHUNK_REPORT_PATH, json.dumps(report, ensure_ascii=False, indent=2))
    return report


def validate_chunks(chunks_path: Path = CHUNKS_PATH) -> dict:
    ids: set[str] = set()
    errors: list[str] = []
    count = 0
    over_hard_max = 0
    with chunks_path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            try:
                chunk = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON: {exc}")
                continue
            count += 1
            chunk_id = chunk.get("chunk_id")
            if not chunk_id:
                errors.append(f"line {line_no}: missing chunk_id")
            elif chunk_id in ids:
                errors.append(f"line {line_no}: duplicate chunk_id {chunk_id}")
            ids.add(chunk_id)
            if not chunk.get("text", "").strip():
                errors.append(f"line {line_no}: empty text")
            source_path = PROJECT_ROOT / chunk.get("source_path", "")
            if not source_path.exists():
                errors.append(f"line {line_no}: missing source_path {source_path}")
            if chunk.get("token_estimate", 0) > HARD_MAX_TOKENS:
                over_hard_max += 1
    return {"chunk_count": count, "unique_ids": len(ids), "errors": errors, "chunks_over_hard_max": over_hard_max}


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit, clean, and chunk processed Markdown files.")
    parser.add_argument("command", choices=["audit", "clean", "chunk", "all", "validate"])
    args = parser.parse_args()

    if args.command == "audit":
        print_audit(audit())
    elif args.command == "clean":
        print(json.dumps(clean(), ensure_ascii=False, indent=2))
    elif args.command == "chunk":
        print(json.dumps(write_chunks(), ensure_ascii=False, indent=2))
    elif args.command == "validate":
        print(json.dumps(validate_chunks(), ensure_ascii=False, indent=2))
    elif args.command == "all":
        print("Audit before clean")
        print_audit(audit())
        print("Clean")
        print(json.dumps(clean(), ensure_ascii=False, indent=2))
        print("Audit after clean")
        print_audit(audit())
        print("Chunk")
        print(json.dumps(write_chunks(), ensure_ascii=False, indent=2))
        print("Validate")
        print(json.dumps(validate_chunks(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
