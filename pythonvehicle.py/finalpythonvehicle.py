"""
Name: finalpythonvehicle.py
Author: Isaac Vahlenkamp
Created: 5/5/2023
Purpose: Drive your new mclaren with a color of your choice maybe with a friend maybe getting chased by police.
"""
#TODO: Import utils for title and int/float
import utils

#TODO: Import random for cops
import random

#TODO: Import sleep so you can read before it returns to menu
from time import sleep

#TODO: Create class for mclaren
class Mclaren_720s:
      #Attributes innit
      def __init__(self, name, color, friend):
            #User name
            self._name = name
            #User Max Speed
            self._max_speed= 212
            #User car color
            self._color= color
            #User speeding tickets allowed
            self._speeding_tickets= 3
            #User friend (y or n)
            self._friend= friend
            #user speed/ starting speed
            self.speed = 75
      #Accelerate
      def accelerate(self):
            #increase speed
            self.speed = self.speed +10
            #check if max speed
            if self.speed > self._max_speed:
                  print("You cannot go any faster")
                  self.speed = self._max_speed
            #print new speed and color
            print(f"You are going {self.speed} mph in your {self._color} Mclaren 720s")
            sleep(1)
            #Check if faster than speed limit
            if self.speed> 75:
                  #if friend create interaction warning(no friend no warning)
                  if self._friend == "y":
                        if self.speed > 75:
                              print("Your friend warns you that cops are ahead")
                              #Warned slow down to speed limit y or n
                              check_speed=input("Would you like to slowdown?(y or n)")
                              if check_speed == "y":
                                    #y self.speed=75
                                    self.speed= 75
                                    #y print statement set to speed limit return 
                                    print(f"Thanks buddy, {self._name} slows down to the speed limit of {self.speed} mph")
                                    self.drive_car()
                              #n check what the cops think
                              elif check_speed == "n":
                                    self.cops()
                  else:
                        #no friend immediate cop chance
                        self.cops()
            #If not faster print statement, return menu
            else:
                  print("That speed increase is amazing!")
                  sleep(1)

      def cops(self):
            #Set range for probabilities 1,10
            pulled_over= random.randrange(1,10)
            #Range 1-5 safe
            if pulled_over in range(1,5):
                  print("The cops seemed to have missed you and you drive by them... You're lucky for now.")
                  sleep(2)
            #Range 6-10 ticket
            elif pulled_over in range(5,10):
                  if self._friend == "y":
                        print("I should have listened to my friend!")
                        print(f"The cops give {self._name} a ticket")
                        self._speeding_tickets = self._speeding_tickets -1
                        #3 tickets = jail
                        if self._speeding_tickets == 0:
                              print("You have recieved three speeding tickets and are going to jail for wreckless driving!")
                              print("Your friend is getting a ride home with the police")
                              quit()
                        else:
                              print(f"You are warned that if you recieve {self._speeding_tickets} more speeding ticket(s) you will go to jail and your new car will be impounded.")
                              sleep(1)
                              self.speed= 75
                  else:
                        print("I should have brought someone to look out for me!")
                        print(f"The cops give {self._name} a ticket")
                        sleep(1)
                        self._speeding_tickets = self._speeding_tickets -1
                        #3 tickets = jail
                        if self._speeding_tickets == 0:
                              print("You have recieved three speeding tickets and are going to jail for wreckless driving!")

                        else:
                              print(f"You are warned that if you recieve {self._speeding_tickets} more speeding ticket(s) you will go to jail and your new car will be impounded.")
                              sleep(1)
            sleep(2)
            self.drive_car()
      
      #Slowdown
      def slow_down(self):
            #decrease speed
            self.speed = self.speed - 10
            #Make so speed cant go negative
            if self.speed < 10:
                  print("You cannot go slower than 10 mph!")
                  self.speed = 10
                  sleep(1)
            else:
                  #print new speed
                  print(f"You slowed down too {self.speed} mph")
                  sleep(1)
                  #If speed lower than speed limit print statements
                  if self.speed< 75:
                        if self._friend == "y":
                              #random friend statements
                              interaction= random.randrange(1,3)
                              if interaction in range(1):
                                    print("You joke with your friend as you cruise safely and enjoy life")
                              elif interaction in range(2):
                                    print("You sing along to music with your friend as you count your blessings")
                              
                              elif interaction in range(3):
                                    print("Your friend and you sit in silence driving safely and enjoying the purr of the engine")
                        #solo statement
                        else:
                              print("Sometimes speed isn't everything you're in the right lane keeping life easy.")
            sleep(2)                 
            self.drive_car

      #
#TODO: Create main METHOD 

      def drive_car(self):
            #TODO: You’re on the interstate speed is 75 {name} speed up 1, slow down 2,  accelerate up or exit 3?
            #print statements to show speed car color
            if self._friend == "y":
                  print(f"\nYou are on the interstate cruising your {self._color} Mclaren 720s at the speed of {self.speed} mph and glad you brought your friend\nHe reminds you the speed limit is 75mph")
            else:
                  print(f"\nYou are on the interstate with your {self._color} Mclaren 720s cruising solo at the speed of {self.speed} mph")
            #TODO: Create choices menu
            car_choices= input("What would you like to do\n1.Accelerate(1)\n2.Slowdown(2)\n3.Go Home(3)\nChoice #:")
            if car_choices== "1":
                  self.accelerate()
                  self.drive_car()
            elif car_choices== "2":
                  self.slow_down()
                  self.drive_car()
            #Let's user go home
            elif car_choices == "3":
                  print("It's time to go home, what a fun time!")
                  quit()

            

#Def Main
def main():
      #Create title
      print(utils.title("Mclaren 720s"))
      #Enter details, of owning 720s and max speed and a couple features
      print("You are about to purchase a Mclaren 720s A car that can go from 0-62mph in 2.9 seconds with a 4 Liter twin turbo charged V8")
      #TODO: Input driver name
      name= input("Please input your name: ")
      #What color will you purchase
      color=input("What color of Mclaren 720s would you like too purchase? ")
      print(f"The color {color} is an excellent choice {name}! Now it is time to take your new ride to the interstate for a joyride")
      #TODO: You are going to cruise in your 720s on the interstate it has two seats pick up a friend?
      friend= input("Would you like to pick up your friend?(y or n) ")
      if friend == "y":
            print(f"You go and pick up your friend he compliments the {color}color and you head to the interstate")
      else:
            print("Maybe some other time! You head to the interstate.")
      #Create car object
      Car= Mclaren_720s(name, color, friend)

      Car.drive_car()
# Else, use as a module
if __name__ == "__main__":
      main()