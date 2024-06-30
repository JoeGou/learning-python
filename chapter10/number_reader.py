from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
print(f"{contents} \t type: {type(contents)}")  #输出的是字符串
numbers = json.loads(contents)
print(f"{numbers} \t type: {type(numbers)}") #输出的是python数据结构，比如此例为列表