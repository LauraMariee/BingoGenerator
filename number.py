from random import *
import os
import yaml


def callNumber(maxNumber):
    value = randint(1, maxNumber)
    return value
    
        
def getCardNumbers(maxCardNum, maxNumber):
    cardNumberList = sample(range(1, maxNumber), maxCardNum)
    return cardNumberList

def getDescription():
    filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'numberDefinitions.yaml')
    with open(filePath) as file:
        desc_list = yaml.load(file, Loader=yaml.FullLoader)
    print(desc_list)



