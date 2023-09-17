n = int(input())
days = n % (24*60)
hours = days//60
minutes = days - hours*60
if hours == 24:
    hours = 0
print(hours, minutes)