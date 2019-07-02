import json
from glob import glob

filenames = glob("../*.ipynb")
filenames = sorted(filenames)


for filename in filenames:
    print("Filename:", filename)
    with open(filename) as inf:
        notebook = json.load(inf)
    new_cells = []
    for cell in notebook['cells']:
        cell_type = cell['cell_type']
        if cell_type == 'markdown':
            new_lines = []
            for line in cell['source']:
                if line.strip().startswith("#"):
                    if "exercise" in line.lower() or "question" in line.lower():
                        line = "#### " + line.replace("#", "").replace(":", "").strip() + "\n"
                    else:
                        if "Introduction" in line:
                            line = "# " + line.replace("#", "").strip() + "\n"
                        elif "Module " in line:
                            line = "## " + line.replace("#", "").strip() + "\n"
                        else:
                            line = "### " + line.replace("#", "").strip() + "\n"
                    print(" ", line.strip())
                new_lines.append(line)

            cell['source'] = new_lines
        new_cells.append(cell)
    notebook['cells'] = new_cells
    with open(filename, 'w') as inf:
        json.dump(notebook, inf, indent=1)

