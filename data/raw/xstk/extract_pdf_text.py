from pathlib import Path

from pypdf import PdfReader


PDFS = {
    "BAIGIANG XS -TK S1.pdf": "bai_01_xac_suat_thong_ke.txt",
    "BAI GIANG XS-TK S2.pdf": "bai_02_cac_quy_tac_tinh_xac_suat.txt",
    "BAIGIANG XS-TK S3.pdf": "bai_03_bien_ngau_nhien.txt",
    "BAI GIANG XS-TK S4.pdf": "bai_04_tham_so_dac_trung_bien_ngau_nhien.txt",
    "BAIGIANG XS-TK S5.pdf": "bai_05_mot_so_luat_phan_phoi_xac_suat_thong_dung.txt",
    "BAI GIANG XS-TK S6.pdf": "bai_06_thong_ke_mo_ta.txt",
    "BAIGIANG XS-TK  S7.pdf": "bai_07_uoc_luong_tham_so.txt",
    "BAIGIANG XS-TK S8.pdf": "bai_08_kiem_dinh_gia_thuyet_thong_ke.txt",
}


def main() -> None:
    base = Path(__file__).resolve().parent
    for pdf_name, txt_name in PDFS.items():
        reader = PdfReader(base / pdf_name)
        parts = []
        for index, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            parts.append(f"\n\n--- PAGE {index} ---\n\n{text}")
        output = "\n".join(parts)
        output = output.replace("\uf0d9", "").replace("\uf0d8", "").replace("\uf04a", "")
        (base / txt_name).write_text(output, encoding="utf-8")
        print(f"{pdf_name}: {len(reader.pages)} pages -> {txt_name} ({len(output)} chars)")


if __name__ == "__main__":
    main()
