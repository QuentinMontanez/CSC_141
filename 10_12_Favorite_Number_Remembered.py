from pathlib import Path
import json

path = Path('fav_number.txt')
contents = path.read_text()
number = json.loads
print(contents)

print(number)
("I know your favorite number! it's _44__")