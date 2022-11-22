class CustomRange:
    
    def __init__(self, string, start, end):
        try:
            stepper_split = string.split("/")
            if len(stepper_split) == 2:
                self.stepper = int(stepper_split[1])
            else:
                self.stepper = 1
            
            number_split = stepper_split[0].split("-")
            if len(number_split) == 2:
                self.last_number = int(number_split[1])
            else:
                if number_split[0] != "*":
                    self.last_number = int(number_split[0])
            
            if number_split[0] == "*":
                self.first_number = start
                self.last_number = end
            else:
                self.first_number = int(number_split[0])
            
            self.numbers = set()
            for i in range(self.first_number, self.last_number+1, self.stepper):
                self.numbers.add(i)
        except Exception as e:
            raise ValueError("Input value is not correct")
        
    def get_numbers(self):
        return self.numbers