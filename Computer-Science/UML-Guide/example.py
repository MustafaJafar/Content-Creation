"""
 Two association relationships, 
 Student —→ City         # association 
 Student —→ Student      # association 
 Student 0* —♢ Section   # Aggregation
 Section 0* —♦ Course    # Composition

 Calculator ⇢ math      # Dependency
 Calculator ⇢ Math      # Dependency

 Shape     —→ Color      # association 
 Rectangle —→ Color      # association 
 Rectangle ──ᐅ Shape    # Inheritance
 
 Human  ╶╶╶ᐅ  Mammal     # Implementation
 Dog    ╶╶╶ᐅ  Mammal     # Implementation
"""

# Forward references "https://peps.python.org/pep-0484/#forward-references" 
# or  
# use annotations "https://stackoverflow.com/questions/61544854/from-future-import-annotations"

from __future__ import annotations
from abc import ABC, abstractmethod

import math 

class City: 
    def __init__ (self , name : str , country: str): 
        self.country = country
        self.name = name 

    def getCountry(self):
        return self.country 
    
    def getName(self):
        return self.name
    
# association "displayed as composition arrow in pynsource!"
class Student: 
    def __init__(self ,  name : str , studentId : int , buddy:Student = None, hometown:City = None ): 
        self.buddy = buddy
        self.hometown = hometown
        self.name = name
        self.studentId = studentId

    def reportBuddyName(self) : 
        if self.buddy :
            return self.buddy.getName() 
        
        return ""
    
    # Get
    def getBuddy(self) -> Student: 
        return self.buddy 
    
    def getHometown(self) -> City:
        return self.hometown
    
    def getName(self):
        return self.name
    
    def getStudentId(self):
        return self.studentId
    
    # Set
    def setBuddy(self , buddy:Student): 
        self.buddy = buddy 

    def setHometown(self,hometown):
        self.hometown = hometown
    
    def setName(self,name):
        self.name = name
    
    def setStudentId(self,studentId):
        self.studentId = studentId
    
# Aggregation "displayed as composition arrow in pynsource!"
class Section: 
    def __init__(self , sectionNum: int , students:list[Student] ) : 
        self.sectionNum = sectionNum
        self.students = students

    def addStudent(self , student :Student ) : 
        self.students.append(student)

    def getStudentById(self , id:int) -> Student: 
        s_filter = lambda student : student.getStudentId() == id
        result =  list(filter( s_filter , self.students ))
        return next(iter(result) , None) 
    
    def getSectionNum(self):
        return self.getSectionNum 
    
    def setSectionNum(self , sectionNum:int): 
        self.sectionNum = sectionNum

# Composition
class Course: 
    def __init__(self, courseNum: str , title:str , sections: list[Section]) : 
        self.courseNum = courseNum
        self.title = title 
        self.sections = sections

    def getCourseNum(self) -> str : 
        return self.courseNum
    
    def getTitle(self) -> str : 
        return self.title
    
    def setCourseNum(self , courseNum: str ): 
        self.courseNum = courseNum 

    def setTitle(self , title : str) : 
        self.title = title 


# Dependency "Not shown in pynsource!"
class Math:
    @staticmethod
    def pow(x ,y ): 
        return x**y 
    
    @staticmethod
    def sqrt(x,y): 
        return x**(1/y)
    
class Calculator: 

    @staticmethod
    def sum(x , y) : 
        return x + y 
    
    @staticmethod
    def subtract (x , y) : 
        return x - y 
    
    @staticmethod
    def power(x,y): # dependant on Math class.
        return Math.pow(x ,y)
    
    @staticmethod
    def sqrt(x,y):
        return Math.sqrt(x,y)
    
    @staticmethod
    def cos(x) : # dependant on math module.
        return math.cos(x)
    
    @staticmethod
    def sin(x) : 
        return math.sin(x)
    
    @staticmethod
    def tan(x) : 
        return math.tan(x)
    
# Inheritance
class Color : 
    def __init__(self , r,g,b) : 
        self.rgb = [r,g,b]

class Shape :
    def __init__(self , color: Color, xCoord : float , yCoord:float ): 
        self.color = Color 
        self.xCoord = xCoord
        self.yCoord = yCoord

    def getCoords (self):
        return (self.xCoord , self.yCoord) 
    
    def getColor(self) : 
        return self.color

class Rectangle(Shape) : 
    def __init__(self , color: Color, xCoord : float , yCoord:float , height : float , width:float ) : 
        super().__init__(color, xCoord , yCoord) 
        self.height = height
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width
    

# Interface Implementation "Abstract base classe "
# you can't instantiate an object from abstract class
class Mammal(ABC):
    @abstractmethod
    def limbs(self) :
        print ("I have 4 limbs") 
    
class Human(Mammal) : 
    def limbs(self) :
        super().limbs()
        print("I have two arms and two legs")

class Dog(Mammal) : 
    def limbs(self) :
        super().limbs()
        print("I have four legs")