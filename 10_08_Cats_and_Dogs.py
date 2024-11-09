from pathlib import Path
path= Path('cats.txt')
contents= path.read_text()
print(contents)
from pathlib import Path
path= Path('dogs.txt')
contents= path.read_text()
print(contents)
try:
    print('cats.txt')
except FileNotFoundError:
 print("No files are missing")