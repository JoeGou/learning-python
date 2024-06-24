from pathlib import Path

def count_word(path, word):
    
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file '{path}' does not exist")
    else:
        words = content.lower().split()
        # words = words.split()
        print(words.count(word))

filenames = ['alice.txt', 'alice2.txt']
for filename in filenames:
    path = Path(filename)
    count_word(path, 'the')