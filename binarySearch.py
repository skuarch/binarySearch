# -*- coding: utf-8 -*-

class Main:

    #===========================================================================
    def __init__(self):
        self.maxNumber = 0
        self.minNumber = 0
        self.isFinished = False
        self.maxLinearQuestions = 4
        self.guessNumber()

    #===========================================================================
    def getUserInput(self, message):
        return raw_input(message)  

    #===========================================================================
    def askLineal(self):
        while (self.getUserInput("your number is " + str(self.minNumber) + " ? y/n ")  == "n") and (self.minNumber <= self.maxNumber):
            self.minNumber +=1    
        return self.minNumber

    #===========================================================================
    def guessNumber(self):

        userInput1 = self.getUserInput("define the maximun number and I will gues a number between that range, positive maximun number: ")        
        self.maxNumber = int(userInput1)
        print(("think in a number between 0 to " + str(self.maxNumber) + ", and I will guess it"))        
        r1 = (self.maxNumber / 2)
        userInput1 = self.getUserInput("your number is " + str(r1) + "? y/n ")
        if(userInput1 == "y"):
            print("tu numero es " + str(r1))
            self.isFinished = True
        else:
            while self.isFinished == False:
                userInput1 = self.getUserInput("your number is greater than " + str(r1) + "? y/n ")
                if(userInput1 == "y"):
                    self.minNumber = r1
                    r1 = (self.maxNumber - self.minNumber) / 2 + self.minNumber

                else:
                    self.maxNumber = r1
                    r1 = (self.maxNumber - self.minNumber) / 2 + self.minNumber

                if((self.maxNumber - self.minNumber)) <= self.maxLinearQuestions:
                        r2 = self.askLineal()
                        print("your number is: " + str(r2))
                        self.isFinished = True

#===========================================================================
main = Main()