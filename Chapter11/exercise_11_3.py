class Employee:
    '''雇员薪资情况'''
    
    def __init__(self, first_name, last_name, annual_salary):
        '''传入姓名与薪资情况'''
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, salary_add=5000):
        ''''默认增加年薪5000美元'''
        self.annual_salary += salary_add
        
        print(f"Congradulations! Your annual salary is {self.annual_salary} now!")
        return self.annual_salary
        
        