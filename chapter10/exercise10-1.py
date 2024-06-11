from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text(encoding='UTF-8').strip()


content_string = ''
for line in contents.splitlines():
    # content_string += line.strip()
    print(line)
# print(contents)

