import number_list

class CronString():
    def __init__(self, string):
        self.raw_string = string
        self.minute = number_list.NumberList(0,59)
        self.hour = number_list.NumberList(0,23)
        self.day_of_month = number_list.NumberList(1,31)
        self.month = number_list.NumberList(1,12)
        self.day_of_week = number_list.NumberList(0,7)
        self.isValid = True

        self.initialize()

    def initialize(self):
        splitted_string = self.raw_string.split(" ")
        if " " in splitted_string:
            splitted_string.remove(" ")

        if len(splitted_string) != 6:
            self.isValid = False
            self.error = "There must be 6 args"
            return

        [minute_string, hour_string, day_of_month_string, month_string, day_of_week_string, self.command] = splitted_string
        if not self.minute.initialize(minute_string):
            self.isValid = False
            self.error = "Error in minute format"
            return
        
        if not self.hour.initialize(hour_string):
            self.isValid = False
            self.error = "Error in hour format"
            return
        
        if not self.day_of_month.initialize(day_of_month_string):
            self.isValid = False
            self.error = "Error in day_of_month format"
            return
        
        if not self.month.initialize(month_string):
            self.isValid = False
            self.error = "Error in month format"
            return
        
        if not self.day_of_week.initialize(day_of_week_string):
            self.isValid = False
            self.error = "Error in day_of_week format"
            return

    def getDetails(self):
        if self.isValid:
            print("minute\t{}".format(self.minute.getNumberList()))
            print("hour\t{}".format(self.hour.getNumberList()))
            print("day_of_month\t{}".format(self.day_of_month.getNumberList()))
            print("month\t{}".format(self.month.getNumberList()))
            print("day_of_week\t{}".format(self.day_of_week.getNumberList()))
            print("command\t{}".format(self.command))
        else:
            print("Not a valid string")
            print(self.error)
