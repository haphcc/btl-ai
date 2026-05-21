from pathlib import Path

from pypdf import PdfReader


FILES = [
    ("Chuong 1_Gioi thieu ve nang luc so.pdf", "chuong_01_gioi_thieu_ve_nang_luc_so.txt"),
    ("Chuong 2_CMCN 4.0 va Chien luoc CDS Quoc gia.pdf", "chuong_02_cmcn_4_0_va_chien_luoc_chuyen_doi_so_quoc_gia.txt"),
    ("Chuong 3_ Khai thac du lieu va thong tin.pdf", "chuong_03_khai_thac_du_lieu_va_thong_tin.txt"),
    ("Chuong 4_ Thiet bi so.pdf", "chuong_04_thiet_bi_so.txt"),
    ("Chuong 5_He dieu hanh.pdf", "chuong_05_he_dieu_hanh.txt"),
    ("Chuong 6_ Mang may tinh va khong gian mang.pdf", "chuong_06_mang_may_tinh_va_khong_gian_mang.txt"),
    ("Chuong 7_Cac ung dung soan thao van ban.pdf", "chuong_07_cac_ung_dung_soan_thao_van_ban.txt"),
    ("Chuong 8_ Bang tinh.pdf", "chuong_08_bang_tinh_dien_tu.txt"),
    ("CHUONG 9_GIAO TIEP VA CONG TAC TREN MTS.pdf", "chuong_09_giao_tiep_va_cong_tac_tren_khong_gian_so.txt"),
    ("CHUONG 10_AN TOAN VA AN SINH SO.pdf", "chuong_10_an_toan_va_an_sinh_so.txt"),
    ("CHUONG 11_SANG TAO NOI DUNG SO.pdf", "chuong_11_sang_tao_noi_dung_so.txt"),
]


def extract_pdf(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    chunks = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n--- PAGE {index} ---\n\n{text}")
    return "".join(chunks)


def main() -> None:
    base = Path(__file__).resolve().parent
    for pdf_name, txt_name in FILES:
        pdf_path = base / pdf_name
        txt_path = base / txt_name
        text = extract_pdf(pdf_path)
        txt_path.write_text(text, encoding="utf-8")
        print(f"{txt_name}: {len(text)} chars")


if __name__ == "__main__":
    main()
