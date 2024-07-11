from exercise_11_3 import Employee
import pytest

@pytest.fixture
def employee1():
    '''可供所有测试函数使用的实例'''
    employee1 = Employee('G', 'Z', 500000)
    return employee1

def test_give_default_raise(employee1):
    '''测试默认加薪'''
    # employee1 = Employee('G', 'Z', 500000)
    employee1.give_raise()
    assert employee1.annual_salary == 505000
    
def test_give_custom_raise(employee1):
    '''测试自定义加薪'''
    # employee1 = Employee('G', 'Z', 500000)
    employee1.give_raise(100000)
    assert employee1.annual_salary == 600000