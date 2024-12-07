from pathlib import Path

source_file = Path(__file__).resolve()
source_folder = source_file.parent
input_path = source_folder / "prenoms.txt"
output_path = source_folder / "prenoms_final.txt"

full_list = []

with open(input_path, "r", encoding='utf-8') as file:
    file_content = file.read().splitlines()
    for line in file_content:
        full_list.extend(line.split())

clean_list = [el.strip("., ") for el in full_list]

with open(output_path, "w", encoding='utf-8') as file:
    file.write("\n".join(sorted(clean_list)))