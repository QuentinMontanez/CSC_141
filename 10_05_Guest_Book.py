user= "Vanessa, Cassiel, Jackson"
while user:
    user= "Entering their names"
from pathlib import Path
path= Path('guest_book.txt')
contents= path.read_text()
