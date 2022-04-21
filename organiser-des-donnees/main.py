from pathlib import Path

source_file = Path(__file__).resolve()
source_folder = source_file.parent
input_path = source_folder / "prenoms.txt"
output_path = source_folder / "prenoms_final.txt"

clean_list = []

with open(input_path, "r", encoding='utf-8') as file:
    file_content = file.read().splitlines()
    for line in file_content:
        new_list = line.split(" ")
        new_list = [i.replace(",","").replace(".","") for i in new_list if any(i)]
        clean_list.extend(new_list)

with open(output_path, "w", encoding='utf-8') as file:
    file.write("\n".join(sorted(clean_list)))