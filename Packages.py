my_package/
init_.py
 module1.py
 module2.py
 main.py 

class ClassOne:
    def _init_(self):
        print("ClassOne Constructor Called")

    def display(self):
        print("Hello from ClassOne")

class ClassTwo:
    def _init_(self):
        print("ClassTwo Constructor Called")

    def display(self):
        print("Hello from ClassTwo")

from .module1 import ClassOne
from .module2 import ClassTwo
# Import classes from the package
from my_package import ClassOne, ClassTwo

# Create objects and call methods
obj1 = ClassOne()
obj1.display()

obj2 = ClassTwo()
obj2.display()