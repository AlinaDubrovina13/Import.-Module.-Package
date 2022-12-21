from datetime import datetime
from Application.salary import calculate_salary
from Application.db.people import get_employees
from flask import Flask

if __name__ == '__main__':
    calculate_salary()
    date = datetime.today()
    print('now', date)

get_employees()
date = datetime.today()
print('now', date)