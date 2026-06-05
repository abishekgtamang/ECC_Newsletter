from pathlib import Path

from PIL import Image, ImageDraw


ASSETS = Path(
    r"C:\Users\Abhishek Ghalan\Documents\Codex\2026-06-05\files-mentioned-by-the-user-evangelical-2\outputs\assets"
)
OUT = Path(
    r"C:\Users\Abhishek Ghalan\Documents\Codex\2026-06-05\files-mentioned-by-the-user-evangelical-2\work\reports-contact-sheet.jpg"
)


def main() -> None:
    files = sorted(ASSETS.glob("reports-page1-image*"))
    sheet = Image.new("RGB", (720, 520), (235, 235, 235))
    for index, file_path in enumerate(files):
        image = Image.open(file_path).convert("RGB")
        image.thumbnail((220, 190))
        x = (index % 3) * 240
        y = (index // 3) * 260
        card = Image.new("RGB", (240, 260), "white")
        card.paste(image, ((240 - image.width) // 2, 14))
        draw = ImageDraw.Draw(card)
        draw.text((8, 224), file_path.name, fill=(0, 0, 0))
        sheet.paste(card, (x, y))
    sheet.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
