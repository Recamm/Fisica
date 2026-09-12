"""Extrae texto de todos los PDF del workspace a archivos .txt espejo en _extraido/."""
import pathlib
import pdfplumber

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_ROOT = ROOT / "_extraido"

def extract_pdf(pdf_path: pathlib.Path, out_path: pathlib.Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            chunks.append(f"\n--- Página {i} ---\n{text}")
    out_path.write_text("".join(chunks), encoding="utf-8")

def main() -> None:
    pdfs = [p for p in ROOT.rglob("*.pdf") if OUT_ROOT not in p.parents]
    print(f"Encontrados {len(pdfs)} PDFs")
    for pdf_path in pdfs:
        rel = pdf_path.relative_to(ROOT)
        out_path = OUT_ROOT / rel.with_suffix(".txt")
        try:
            extract_pdf(pdf_path, out_path)
            size = out_path.stat().st_size
            flag = "VACIO/POSIBLE ESCANEO" if size < 50 else "ok"
            print(f"[{flag}] {rel} -> {size} bytes")
        except Exception as e:
            print(f"[ERROR] {rel}: {e}")

if __name__ == "__main__":
    main()
