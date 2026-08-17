# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## The Approach
For this discussion I created Server as the parent class and UnbuntuServer as child class. I chose this due to a project
of mine at work involves me building a server. The UnbuntuServer class comes with common server information and 
functionality while also having some Unbuntu features.


## Implementation of Requirements

Complete all TODO sections in the source code:

1. **Parent Class:** Created Server with class and instance variables, constructor, and a get_info() method.
2. **Child Class:** Created UnbuntuServer using inheritance. It adds Unbuntu variables and methods and overrides get_info()
3. **Namespaces:** Created two Unbuntu server objects and demonstrated class variables, instance variables, __dict__, and
an attribute added to only one object.
4. **Copying:** Created shallow and deep copies of a server containing nested mutable configuration data and demonstrated 
how changing the original affects the shallow copy, but not the deep copy.
5. **Main:** Created and tested both parent and child objects and called the namespace and copying functions.
6. **Student Extension:** Added add_service() method that allows a service to be added to a server.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.