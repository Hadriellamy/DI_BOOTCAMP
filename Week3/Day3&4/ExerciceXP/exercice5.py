#Exercise 5 : Amount Of Time Left Until January 1st
"""
Instructions

Create a function that displays the amount of time left from now until January 1st.
(Example: the 1st of January is in 10 days and 10:34:01hours).

"""

from datetime import datetime, timedelta

def time_until_january_first():
    now = datetime.now()
    next_jan_1st = datetime(year=now.year + 1, month=1, day=1)
    delta = next_jan_1st - now

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days, {hours:02}:{minutes:02}:{seconds:02} hours.")

time_until_january_first()
