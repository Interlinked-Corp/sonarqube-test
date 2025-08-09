import math

def greet(name):
    print("Hello, " + name)
    pass

def calculate_area(radius):
    return 3.14 * radius * radius

def unused_variable():
    x = 10
    y = 20
    return 5

def unused_parameter(a, b, c):
    return a + b

def remove_private_method():
    _private_method()

def _private_method():
    print("This is a private method, but never used.")

def unused_local_variable():
    temp = "temp"
    return "Result"

def class_with_unused_method():
    class MyClass:
        def used_method(self):
            print("This method is used")
            pass  # Intentionally useless for SonarQube to detect
        
        def unused_method(self):
            print("This method is not called")
    
    obj = MyClass()
    obj.used_method()

def unused_scope_limited_definition():
    def helper():
        local_var = 42
        pass
    helper()

greet("World")
calculate_area(5)
unused_variable()
unused_parameter(2, 3, 4)
remove_private_method()
unused_local_variable()
class_with_unused_method()
unused_scope_limited_definition()