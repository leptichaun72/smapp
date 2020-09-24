import os
from pytz import timezone

#define Eastern timezone
eastern = timezone('US/Eastern')

project_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(project_dir, "usetoilet.db"))

