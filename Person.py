from typing import Any
from Fibonacci import Fibonacci
class Person:
    def __init__(self,name,AOD,YOD):
        self.name = name
        self.AOD = AOD
        self.YOD = YOD
        # self.name = input('Enter your name: ')
        # self.AOD = int(input('Enter Age of Death: '))
        # self.YOD = int(input('Enter Year of Death: '))
    
    def showPerson(self):
        print("Person", self.name, "born on Year = ", self.YOD ,'–', self.AOD, '=', self.YOD - self.AOD, 
              "number of people killed on year", self.YOD - self.AOD, "is", end=' ' )
    