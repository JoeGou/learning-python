from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text(encoding='UTF-8').strip()


content_string = ''
for line in contents.splitlines():
    # content_string += line.strip()
    line = line.replace('Chapter', 'python chapter')
    content_string += line
    print(line)
    

print(content_string)