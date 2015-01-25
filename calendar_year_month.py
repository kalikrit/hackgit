import bottle
import html
import calendar
from datetime import datetime

# индексный раут - localhost:8080/
@bottle.route('/')
def index():
    c = calendar.HTMLCalendar()
    now = datetime.now()
    return c.formatyearpage(now.year, width=3)

# год localhost:8080/year/<year>
# year - чило от 1900-3001
# если не в этом интервале, то будет отображен текущий год	
@bottle.route('/year/<year>')
def print_year(year=None):
    c = calendar.HTMLCalendar()
    year = html.escape(year)
    try:
        year = int(year)
    except:
        print("Error in data type (year)")
        
    years = [x for x in range(1900,3001)]
    if year not in years:
        now = datetime.now()
        year = now.year
    return c.formatyearpage(year, width=3)

# месяц localhost:8080/month/<month>
# календарь на месяц текущего года
# месяц в интервале [1-12]
# если не этом интервале будет отображен текущий месяц текущего года
# todo: сделать чтобы работала комбинация год/месяц для отображения месяца любого года
@bottle.route('/month/<month>')
def print_month(month=None):
    c = calendar.HTMLCalendar()
        
    month = html.escape(month)
    try:
        month = int(month)
    except:
        print("Error in data type (month)")
        
    months = [x for x in range(1,13)]
    now = datetime.now()
    if month not in months:
        month = now.month
        
    return c.formatmonth(theyear=now.year, themonth=month)

bottle.debug(True)
bottle.run(host='localhost', port=8080)	