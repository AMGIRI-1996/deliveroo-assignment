from cron_subexpression import CronSubexpression

class CronExpression():
    def __init__(self, raw_string):
        self.raw_string = raw_string

        splitted_string = self.raw_string.split(" ")
        if " " in splitted_string:
            splitted_string.remove(" ")

        if len(splitted_string) != 6:
            raise ValueError("There must be 6 args")

        [minute_string, hour_string, day_of_month_string, month_string, day_of_week_string, self.command] = splitted_string
        self.minute = CronSubexpression(0,59,minute_string)
        self.hour = CronSubexpression(0,23,hour_string)
        self.day_of_month = CronSubexpression(1,31,day_of_month_string)
        self.month = CronSubexpression(1,12,month_string)
        self.day_of_week = CronSubexpression(0,7,day_of_week_string)

