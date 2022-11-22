import sys
from cron_expression import CronExpression
from cron_printer import CronPrinter

if __name__ == '__main__':
    cron_object = CronExpression(sys.argv[1])
    CronPrinter.print_cron_string(cron_object)
