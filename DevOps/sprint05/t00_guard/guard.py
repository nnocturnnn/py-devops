
class Guard:
    def __init__(self, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = None
        if 'salary' in kwargs:
            self.salary = kwargs['salary']
        else:
            self.salary = 0
        
    def greet(self):
        return f"Hello, my name is {self.name}!"

    def receive_bribe(self, num):
        if self.salary < num:
            return 'You may pass.'
        else:
            return 'I am not letting you pass.'
