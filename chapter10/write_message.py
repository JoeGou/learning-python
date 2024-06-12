from pathlib import Path

contents = 'I love programming.\n'
contents += 'I love creating games.\n'
contents += 'I also love working with data.\n'

path = Path('programming.txt')
path.write_text(contents)
contents_read = path.read_text()
print(contents_read)