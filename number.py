from random import *
import os
import yaml
import typing


class Number:

    number: int
    description: str
    explanation: str

    def __init__(self, number, description, explanation):
        self.number = number
        self.description = description
        self.explanation = explanation
        
    @staticmethod
    def callNumber(maxNumber):
        number = randint(1, maxNumber)
        return number
        
    @staticmethod
    def getCardNumbers(maxCardNum, maxNumber):
        cardNumberList = sample(range(1, maxNumber), maxCardNum)
        return cardNumberList

    @staticmethod
    def getDescription(num):
        filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'numberDefinitions.yaml')
        with open(filePath) as stream:
            desc_list = yaml.load(stream, Loader=yaml.FullLoader).get("numbers")
            for entry in desc_list:
                if entry.get("number") == num:
                    return entry.get("desc")

    @staticmethod
    def loadNumbers(file_name: typing.Optional[str] = None) -> typing.Dict[int, 'Number']:
        """
        Loads all the numbers from the yaml file with the number definitions.

        By default, it loads the file "numberDefinitions.yaml", but you can pass any
        file name to it in case you want to load a different file.

        Returns a dictionary, that maps the actual number to a `Number` object containing the
        description and explanation for that number.

        Example usage:

        Loading `numberDefinitions.yaml` into "numbers":
        >>> numbers = Number.loadNumbers()

        It is easy to get the `Number` object for the number you are interested in:
        >>> three = numbers[3]
        >>> three.number
        3
        >>> three.description
        'Cup of tea'
        >>> three.explanation
        "Rhymes with 'Three'"

        """

        # default filename is the 'numberDefinitions.yaml' next to this python file
        # unless you decide to load any other file
        if file_name is None:
            folder = os.path.dirname(__file__)
            file_name = os.path.join(folder, "numberDefinitions.yaml")

        # open file and load yaml
        with open(file_name) as f:
            yaml_contents = yaml.load(f, Loader=yaml.SafeLoader)

        # turn the yaml structure into instances of the `Number` class
        numbers = []
        yaml_numbers = yaml_contents["numbers"]
        for yaml_number in yaml_numbers:
            try:
                number = Number(
                    number=yaml_number["number"],
                    description=yaml_number["desc"],
                    explanation=yaml_number["explanation"],
                )
            except KeyError:
                # When something goes wrong, we raise an exception with a helpful description
                # instead of a nasty KeyError, with some extra info to make it easier to find the 
                # line in the yamlfile, that causes the problem.
                raise Exception("The yaml file contains an invalid number. "
                    "Every number must have the fields 'number', 'desc' and 'explanation'. "
                    f"The erroneous entry is this one: {yaml_number}")
            numbers.append(number)

        # put the numbers into a dictionary, so that they can be accessed by their actual number:
        numbers_dict = dict()
        for number in numbers:
            numbers_dict[number.number] = number

        return numbers_dict
