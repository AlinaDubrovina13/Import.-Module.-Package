from datetime import *
from Application.salary import *
from Application.db.people import *
from flask import *

if __name__ == '__main__':
    calculate_salary()
    date = datetime.today()
    print('now', date)