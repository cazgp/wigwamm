import datetime
from datetime import date, timedelta
import shortuuid
import uuid

def make_uuid():
    return shortuuid.uuid()

def weeks_range(today, num_weeks):
    first_monday = today - timedelta(days=today.weekday())
    num_days = num_weeks * 7
    dates = (first_monday + timedelta(days=x) for x in range(0, num_days))
    return dates
