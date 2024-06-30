from name_function import get_formmated_name

def test_first_last_name():
    '''能够正确处理像Janis Joplin这样的名字吗?'''
    formatted_name = get_formmated_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    '''能够正确处理像Wolfgang amadeus  mozart这样的名字吗?'''
    formatted_name = get_formmated_name('wolfgang', 'amadeus', 'mozart')
    assert formatted_name == 'Wolfgang Mozart Amadeus'