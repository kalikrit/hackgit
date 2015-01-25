import bottle
import html
import calendar
from datetime import datetime

@bottle.route('/')
def index():
    c = calendar.HTMLCalendar()
    now = datetime.now()
    return c.formatyearpage(now.year, width=3)

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