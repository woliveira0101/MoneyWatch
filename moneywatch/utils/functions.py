import datetime
import math

from calendar import monthrange



def get_date_from_string(date, format):

    return datetime.datetime.strptime(date, format).date()
    
def get_date_from_days(days):

    date_unix = datetime.date(1970,1,1)
    date_target = date_unix + datetime.timedelta(days=days)
    return date_target
    
def get_days_from_date(date):
    if date is None:
        return 0
    
    date_unix = datetime.date(1970,1,1)
    date_target = date - date_unix
    return date_target.days

    
def get_first_day_of_month(year=None, month=None):


    date_today = datetime.date.today()
    date_month = date_today.month
    date_year = date_today.year
    
    if month:
        date_month = month
    if year:
        date_year = year
    
    
    date_first = datetime.date(date_year,date_month,1)

    return date_first
    
def get_last_day_of_month(year=None,month=None):
    date_first = get_first_day_of_month()
    
    date_last_year = date_first.year
    date_last_month = date_first.month
    
    if year:
        date_last_year = year
    
    if month:
        date_last_month = month
    
    if date_last_month == 12:
        date_last_year += 1
        date_last_month = 1
    else:
        date_last_month += 1
    
    
    date_first_next = datetime.date(date_last_year,date_last_month,1)
    date_last_month = date_first_next - datetime.timedelta(days=1)
    
    return date_last_month

def get_number_of_months(start=None, end=None):

    start_date = get_first_day_of_month()
    end_date = get_last_day_of_month()
    
    if start:
        start_date = start
        
    if end:
        end_date = end

    diff = _monthdelta(start_date,end_date)
    
    return int(math.ceil(diff))

def _monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]

        d1 += datetime.timedelta(days=mdays)
        if d1 < d2:
            delta += 1
        elif d1 == d2:
            delta += 1
            break
        else:
            break
    
    if d1 > d2:
        diff = d1 - d2
        delta += (monthrange(d2.year, d2.month)[1] - diff.days) / monthrange(d2.year, d2.month)[1]

    return delta
       
    
def add_months(date, months):
    date_new = date 
    for i in range(months):   
        year = date_new.year
        month = date_new.month
        day = date_new.day
        maxdays_before = monthrange(year, month)[1]
        
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

        maxdays_after = monthrange(year, month)[1]
        
        # avoid 31.10 => 31.11 (does not exist, last day in november is 30.11)
        if day == maxdays_before or day > maxdays_after:
            date_new = datetime.date(year,month,maxdays_after)
       
        else:  
            date_new = datetime.date(year,month,day)
    
    return date_new


def substract_months(date, months):

    for i in range(months):   
        year = date.year
        month = date.month
        day = date.day
        maxdays_before = monthrange(year, month)[1]
        
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
        
        
        maxdays_after = monthrange(year, month)[1]
        
        # avoid 31.10 => 31.11 (does not exist, last day in november is 30.11)
        if day == maxdays_before or day > maxdays_after:
            date = datetime.date(year,month,maxdays_after)
       
        else:  
            date = datetime.date(year,month,day)
    
    return date
  

def is_same_month_in_list(days, list):

    result = False
    for item in list:
        if _is_same_month(days, item):
            result = True
            break
            
    return result

    
def _is_same_month(date1, date2):

    return True if date1.year == date2.year and date1.month == date2.month else False


  
def get_cyclic_dates_for_timerange(date, months_interval, start, end):

    result = []

    while True:

        if date >= start and date <= end:

            result.append(date)

        date = add_months(date, months_interval)
    
        if date > end:
            break
    
    return result
    

        