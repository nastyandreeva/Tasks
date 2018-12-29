from random import randint
def deco(func):
  import functools
  import time
  @functools.wraps(func)
  def inner(*args, **kwargs):
    start_time = time.time()  # начало таймера
    result = func(*args, **kwargs)
    end_time = time.time()  # завершение таймера
    time_delta = end_time - start_time
    with open('test.txt', 'a') as f:
       f.write(f'Время выполнения функции {func.__name__} заняло: {time_delta:.5}\n')
    return result
  return inner

@deco
def two_sum_brute(nums, target):  
  length = len(nums)
  for i in range(length):
    for j in range(i+1, length):
      if nums[j] == target - nums[i]:
        return [i, j]


"""
one-pass hash-table
"""
@deco
def two_sum(nums, target):
  dic = {}
  for index, num in enumerate(nums): 
    n = target - num    
    if n not in dic:
      dic[num] = index      
    else:
      return [dic[n], index]  

numbers = []
for i in range(1000000):
    numbers.append(randint(-100, 100))

if __name__ == "__main__":
  print(two_sum_brute(numbers, 9))
  print(two_sum(numbers, 9))
