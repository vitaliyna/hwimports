import argparse
from datetime import datetime
import random

datenow = datetime.now()
dategoal = datetime(day=1, month=1, year=2023)
datedelta = dategoal - datenow
list_of_toy = ['Red ball', 'Black gun', 'Color pyramid', 'Funny book', 'White car', 'Music helicopter']
random_index = random.randint(0, len(list_of_toy) - 1)

parser = argparse.ArgumentParser(description="Считает количество дней до нового года")
parser.add_argument('newyear', type = str, help = 'выводит количетво дней до нового года')
parser.add_argument('--hour', action="store_true", help = 'выводит количетво часов до нового года')
args = parser.parse_args()

if args.newyear == 'toy':
    print(list_of_toy[random_index])
else:
    if args.hour:
       print(f'{datedelta.days} дней {datedelta.seconds // 3600} часов')
    else:
       print(f'{datedelta.days} дней')