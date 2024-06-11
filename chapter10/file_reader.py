from pathlib import Path

#Absolute path
# path = Path(r'C:\Users\zhuang.gou\Desktop\python_work\chapter10\pi_digits.txt')

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

# lines = contents.splitlines()
for line in contents.splitlines():
    print(line)

