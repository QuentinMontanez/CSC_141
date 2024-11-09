from pathlib import Path
path = Path('learning C.txt')
contents = path.read_text()
print(contents)
path.replace('C')