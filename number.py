from random import *
import os
import yaml



class Number:
    
    description = "Default"
    number = "Default"
    
    def __init__(self, **entries): 
        self.__dict__.update(entries)
        
    def callNumber(maxNumber):
        number = randint(1, maxNumber)
        return number
        
    def getCardNumbers(maxCardNum, maxNumber):
        cardNumberList = sample(range(1, maxNumber), maxCardNum)
        return cardNumberList

    def getDescription(num):
        filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'numberDefinitions.yaml')
        with open(filePath) as stream:
            desc_list = yaml.load(stream, Loader=yaml.FullLoader).get("numbers")
            for entry in desc_list:
                if entry.get("number") == num:
                    return entry.get("desc")
                



