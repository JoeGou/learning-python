from exercise_10_1 import get_formmated_city_country 

def test_city_country():
    '''测试Santiago chile是否能正常输出'''
    formatted_name = get_formmated_city_country('santiago', 'chile')
    assert formatted_name == 'Santiago Chile'

def test_city_country_population():
    '''测试Santiago chile是否能正常输出'''
    formatted_name = get_formmated_city_country('santiago', 'chile', 5000000)
    assert formatted_name == 'Santiago, Chile - population 5000000'