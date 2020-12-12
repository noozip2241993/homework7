import random
import statistics
from collections import Counter

#set a ramdom seed generator
random.seed(2020)
#set number of integers
integers = 20
random_number= [random.randrange(100,121) for _ in range(integers)]
sort_random_number = sorted(random_number)
print(sort_random_number)
count_numbers = len(sort_random_number)//2
Median = (sort_random_number[count_numbers - 1] + sort_random_number[count_numbers])/2
print(f'Mannually Median is {Median}')
test_median = statistics.median(random_number)
print(f'Statistics module Median is {test_median}')

#set a unique list
unique_list = set(sort_random_number)
data = Counter(sort_random_number)
print(data)
get_mode = dict(data)

mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
print(f'Mannually Mode is {mode}')
test_mode = statistics.mode(random_number)
print(f'Statistics module Mode is {test_mode}')

list_all_mode = [k for k, v in get_mode.items() if v >= 2]
print(f'Two or more number have the same frequency:\n{list_all_mode}')