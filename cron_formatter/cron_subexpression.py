from custom_range import CustomRange
class CronSubexpression:

    def __init__(self, lower_limt, upper_limt, raw_string):
        self.lower_limt = lower_limt
        self.upper_limt = upper_limt
        self.numbers = None
        self.range_list = []

        number_ranges = raw_string.split(",")
        for number_range in number_ranges:
            self.range_list.append(CustomRange(number_range, self.lower_limt, self.upper_limt))

    def getNumberList(self):
        if self.numbers != None:
            return self.numbers
        
        number_set = set()
        for ranges in self.range_list:
            number_set.update(ranges.get_numbers())
        
        self.numbers = sorted(number_set)
        return self.numbers
    