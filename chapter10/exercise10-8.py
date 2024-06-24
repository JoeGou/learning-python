from pathlib import Path

def read_file(path):
    '''读取文件内容'''
    try:
        category = path.read_text().splitlines()
        print(f"\n{path} has many cut pets: ")
        for item in category:
            print(f" {item}" )
    except FileNotFoundError:
        #print(f"The '{path}' is not found") 
        pass
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
     path = Path(filename)    
     read_file(path)