#!/usr/bin/env python
import random
from user import User
class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        return random.choice(self.knowledge)

     
     # The knowledge list provided
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

# Create a Teacher instance with the provided knowledge
knowledge = "Mathematics"
teacher = Teacher("John", "Doe", knowledge)

# Access attributes
print(teacher.first_name)    # Output: John
print(teacher.last_name)     # Output: Doe
print(teacher.knowledge)     # Output: The list of knowledge strings