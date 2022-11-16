import sys
import cron_string



if __name__ == '__main__':
    cron_object = cron_string.CronString(sys.argv[1])
    cron_object.getDetails()
