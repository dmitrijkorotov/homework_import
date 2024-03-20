import wikipedia
from datetime import date
from application.db.people import get_employees
from application.salary import calculate_salary


def current_date():
    return date.today().strftime("%d-%m-%Y")

def info(text):
    wikipedia.set_lang("ru")
    print(wikipedia.summary(text, sentences=2))

if __name__ == "__main__":
    info('Бухгалтерия')
    print(f'\nCегодня: {current_date()}')
    get_employees('Петрович')
    calculate_salary(50000)