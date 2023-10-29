from datetime import timedelta, date

yesturady = date.today() - timedelta(days=1)
today = date.today()
tomorrow = date.today() + timedelta(days=1)
print(yesturady)
print(today)
print(tomorrow)