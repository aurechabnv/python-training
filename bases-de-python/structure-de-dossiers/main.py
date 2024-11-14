from pathlib import Path

source_path = Path(__file__).resolve() 
target_path = source_path.parent / "data"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for parent_folder, inner_folders in d.items():
    for inner_folder in inner_folders:
        folder_path = target_path / parent_folder / inner_folder
        folder_path.mkdir(exist_ok=True, parents=True)