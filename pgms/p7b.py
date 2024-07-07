class A:
    def __init__(self):
        self.lst = []  # Initialize an empty list
        self.n = int(input("Enter an integer value for n: "))  # Prompt user for n

    def function(self):
        self.lst.append(self.n)  # Append n to lst


class B(A):
    def __init__(self):
        super().__init__()  # Call parent class constructor
        self.lst1 = []  # Initialize an empty list for lst1
        self.n1 = int(input("Enter an integer value for n1: "))  # Prompt user for n1
        self.n2 = int(input("Enter an integer value for n2: "))  # Prompt user for n2

    def function(self):
        super().function()  # Call parent class function
        self.lst1.append(self.n1)  # Append n1 to lst1
        self.lst1.append(self.n2)  # Append n2 to lst1
