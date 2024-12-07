from pathlib import Path

dirs = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Vidéos",
    ".mp4": "Vidéos",
    ".gif": "Vidéos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents"
}

SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent
DATA_DIR = SOURCE_DIR / "data"

files_to_file = [f for f in DATA_DIR.iterdir() if f.is_file()]

for f in files_to_file:
    output_dir = DATA_DIR / dirs.get(f.suffix, "Divers")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)