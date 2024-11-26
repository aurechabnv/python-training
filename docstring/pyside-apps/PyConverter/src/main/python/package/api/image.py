from pathlib import Path

from PIL import Image

class CustomImage:
    def __init__(self, path, folder="reduced"):
        self.image = Image.open(path)
        self.width, self.height = self.image.size
        self.path = Path(path)
        self.reduced_path = self.path.parent / folder / self.path.name

    def reduce_size(self, size=0.5, quality=75):
        new_width = round(self.width * size)
        new_height = round(self.height * size)
        self.image = self.image.resize((new_width, new_height), Image.LANCZOS)
        Path.mkdir(self.reduced_path.parent, parents=True, exist_ok=True)
        self.image.save(self.reduced_path, 'JPEG', quality=quality)
        return self.reduced_path.exists()