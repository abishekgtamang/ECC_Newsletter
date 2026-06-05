from math import ceil
from pathlib import Path

from PIL import Image, ImageDraw


ASSETS = Path(
    r"C:\Users\Abhishek Ghalan\Documents\Codex\2026-06-05\files-mentioned-by-the-user-evangelical-2\outputs\assets"
)
OUT = Path(
    r"C:\Users\Abhishek Ghalan\Documents\Codex\2026-06-05\files-mentioned-by-the-user-evangelical-2\work\asset-contact-sheet.jpg"
)


def main() -> None:
    thumbs = []
    for file_path in sorted(ASSETS.glob("*")):
        image = Image.open(file_path).convert("RGB")
        image.thumbnail((220, 150))
        canvas = Image.new("RGB", (240, 200), "white")
        canvas.paste(image, ((240 - image.width) // 2, 12))
        draw = ImageDraw.Draw(canvas)
        draw.text((8, 174), file_path.name, fill=(0, 0, 0))
        thumbs.append(canvas)

    sheet = Image.new("RGB", (720, ceil(len(thumbs) / 3) * 200), (230, 230, 230))
    for index, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((index % 3) * 240, (index // 3) * 200))
    sheet.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
