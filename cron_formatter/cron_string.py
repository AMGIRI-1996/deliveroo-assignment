import number_list

class CronString():
    def __init__(self, string):
        self.raw_string = string
        self.minute = number_list.NumberList(0,59)
        self.hour = number_list.NumberList(0,23)
        self.day_of_month = number_list.NumberList(1,31)
        self.month = number_list.NumberList(1,12)
        self.day_of_week = number_list.NumberList(0,7)
        self.is_valid = True

        self.initialize()

    def initialize(self):
        splitted_string = self.raw_string.split(" ")
        if " " in splitted_string:
            splitted_string.remove(" ")

        if len(splitted_string) != 6:
            self.setError("There must be 6 args")
            return

        [minute_string, hour_string, day_of_month_string, month_string, day_of_week_string, self.command] = splitted_string
        self.minute.initialize(minute_string)
        self.hour.initialize(hour_string)
        self.day_of_month.initialize(day_of_month_string)
        self.month.initialize(month_string)
        self.day_of_week.initialize(day_of_week_string)  

    def getDetails(self):
        if self.is_valid:
            print("minute\t{}".format(self.minute.getNumberList()))
            print("hour\t{}".format(self.hour.getNumberList()))
            print("day_of_month\t{}".format(self.day_of_month.getNumberList()))
            print("month\t{}".format(self.month.getNumberList()))
            print("day_of_week\t{}".format(self.day_of_week.getNumberList()))
            print("command\t{}".format(self.command))
        else:
            print("Not a valid string")
            print(self.getError())

    def setError(self, description):
        self.is_valid = False
        self.error = description
    
    def isValid(self):
        if self.is_valid:
            if not self.minute.isValid():
                self.setError("Error in minute format")

            elif not self.hour.isValid():
                self.setError("Error in hour format")

            elif not self.day_of_month.isValid():
                self.setError("Error in day_of_month format")

            elif not self.month.isValid():
                self.setError("Error in month format")

            elif not self.day_of_week.isValid():
                self.setError( "Error in day_of_week format")

        return self.is_valid
    
    def getError(self):
        return self.error
