#!/usr/bin/env python

from user import User

class Student(User):
     def __unit__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = []

     def learn(self, subject):
        self.knowledge.append(subject)