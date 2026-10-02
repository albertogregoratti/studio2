import json
import glob

# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell.
# Use it to list files matching wildcards like *.py, data-??.csv inside directories.

from pathlib import Path

input_dir = "C:/Temp/fd_files_in"
output_file = "C:/Temp/fd_files_out.json"

with open(output_file, "w", encoding="utf-8") as out:
    for path in Path(input_dir).glob("*.json"):
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                for obj in data:
                    out.write(json.dumps(obj, ensure_ascii=False) + "\n")
            else:
                out.write(json.dumps(data, ensure_ascii=False) + "\n")