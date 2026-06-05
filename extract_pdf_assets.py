from pathlib import Path

from pypdf import PdfReader


PDF_PATH = Path(r"C:\Users\Abhishek Ghalan\Downloads\Evangelical CHristian Coll.pdf")
OUT_DIR = Path(
    r"C:\Users\Abhishek Ghalan\Documents\Codex\2026-06-05\files-mentioned-by-the-user-evangelical-2\outputs\assets"
)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(PDF_PATH)
    count = 0
    for page_number, page in enumerate(reader.pages, start=1):
        for image in page.images:
            count += 1
            extension = Path(image.name).suffix or ".png"
            destination = OUT_DIR / f"page{page_number}-image{count}{extension}"
            destination.write_bytes(image.data)
            print(f"{destination} {len(image.data)}")
    print(f"count {count}")


if __name__ == "__main__":
    main()
