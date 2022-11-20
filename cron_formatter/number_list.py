class NumberList():

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.numbers = set()
        self.is_valid = True
    
    def initialize(self, raw_string):
        try: 
            number_ranges = raw_string.split(",")
            for number_range in number_ranges:
                self.addNumbersToList(number_range)
        except Exception as e:
            print(e)
            self.setError(e)

    def addNumbersToList(self,number_range):
        stepper_split = number_range.split("/")
        if len(stepper_split) == 2:
            stepper = int(stepper_split[1])
        else:
            stepper = 1
        
        number_split = stepper_split[0].split("-")
        if len(number_split) == 2:
            last_number = int(number_split[1])
        else:
            if number_split[0] != "*":
                last_number = int(number_split[0])
        
        if number_split[0] == "*":
            first_number = self.start
            last_number = self.end
        else:
            first_number = int(number_split[0])
        
        for i in range(first_number, last_number+1, stepper):
            self.numbers.add(i)

    def getNumberList(self):
        return sorted(self.numbers)
    
    def setError(self, description):
        self.is_valid = False
        self.error = description
    
    def isValid(self):
        return self.is_valid

    def getError(self):
        return self.error
    