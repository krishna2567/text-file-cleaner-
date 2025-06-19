import re
import sys
from pathlib import Path

WHITESPACE_RE = re.compile(r'\s+')  
def clean_extra_spaces(input_path: Path, output_path: Path) -> None:
    with input_path.open('r', encoding='utf-8') as fin, \
         output_path.open('w', encoding='utf-8') as fout:
        for raw in fin:
            stripped = raw.strip()
            if not stripped: 
                continue
            normalised = WHITESPACE_RE.sub(' ', stripped)
            fout.write(normalised + '\n')  
    print(f"✅ Cleaned file saved to {output_path.resolve()}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python clean_txt.py <input_file> <output_file>")
    clean_extra_spaces(Path(sys.argv[1]), Path(sys.argv[2]))