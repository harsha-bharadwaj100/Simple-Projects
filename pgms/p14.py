class Person:
    def __init__(self, name, age) -> None:
        self.age = age
        self.name = name


class Employee(Person):
    def __init__(self, name, age, employee_id) -> None:
        super().__init__(name, age)
        self.employee_id = employee_id


emp1 = Employee(name="John Doe", age=24, employee_id=23465)
print(f"Name: {emp1.name}")
print(f"Age: {emp1.age}")
print(f"Employee ID: {emp1.employee_id}")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Employee(Person):
#     def __init__(self, name, age, employee_id):
#         super().__init__(name, age)
#         self.employee_id = employee_id


# # Create an instance of Employee
# employee1 = Employee(name="John Doe", age=30, employee_id="E12345")

# # Print details
# print(f"Name: {employee1.name}")
# print(f"Age: {employee1.age}")
# print(f"Employee ID: {employee1.employee_id}")
