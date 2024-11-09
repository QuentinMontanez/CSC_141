user= input("Please write your name here")
from pathlib import Path
path= Path('guest.txt')
contents = path.read_text()