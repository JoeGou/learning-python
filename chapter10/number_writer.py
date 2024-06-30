from pathlib import Path
import json

numbers = [2, 3, 5, 7, 9, 11, 13]

path = Path('numbers.json')  #指定存储路径
contents = json.dumps(numbers)
path.write_text(contents)