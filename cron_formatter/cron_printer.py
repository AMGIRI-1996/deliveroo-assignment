from cron_expression import CronExpression
class CronPrinter:
    @staticmethod
    def print_cron_string(cron_expression_obj:CronExpression):
        print("minute\t{}".format(cron_expression_obj.minute.getNumberList()))
        print("hour\t{}".format(cron_expression_obj.hour.getNumberList()))
        print("day_of_month\t{}".format(cron_expression_obj.day_of_month.getNumberList()))
        print("month\t{}".format(cron_expression_obj.month.getNumberList()))
        print("day_of_week\t{}".format(cron_expression_obj.day_of_week.getNumberList()))
        print("command\t{}".format(cron_expression_obj.command))