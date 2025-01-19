"""
https://www.youtube.com/watch?v=uNLNQKGojc8
The single-responsibility principle states that:

A class should have only one reason to change.

This means that a class should have only one responsibility, as expressed through its methods.
If a class takes care of more than one task, then you should separate those tasks into separate classes.
"""


# Q. what is single responsibilty principle?
# Ans. Any module (can be a set of functions, class, package, source code) should have a reason to change
#  by only one actor or the whole functionality should be able to change by only one actor.

# lets imagine a scenario where calculateSalary and calculateHours using some same private method gethours
# if there is any kind of calculation change in calculatesalary method in this class and it might require a change in
# change in gethours private method, now both method are changed now since calculatehours also using gethours 
# method internally this implementation breaks
# cfo required a change and the HR department is getting some wrong data because the somebody has changed the 
# method which is required by the both public method 
# so here is one employee class exposed 2 or 3 methods which were corresponsding to different stakeholder
# of the software, one actor doesn't have to know anything about the other actor but still change requested 
# from one of them and has impacted the other one. 
# now this here is breaking the rule of single responsibility principle beacuse this class encapsulated with the 
# different method of the different funcationality which cater to different actor.

# In single responsibilty principle that code you are writing if that code changes from one actor or group of actor 
# which fulfil one business requirement till that point it is fine

# so, best solution for this, breaking down one class to multiple class with one business functionality without 
# breaking any exiting functionality
# benefit of using SRP: is improved code clarity, easier maintenance, better testability, and reduced risk of introducing bugs 
# when making changes, as each class handles only one specific responsibility.

class Employee:
    
    def gethours():
        pass
class CalculateSalary(Employee):
    def gethours(self):
        pass
    
# this method can be used by HR
class CalculateHours(Employee):
    def gethours(self):
        pass

# this method can be used by technical person
class SaveEmpData(Employee):
    def gethours(self):
        pass
