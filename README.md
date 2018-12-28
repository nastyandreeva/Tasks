# Задание №1
Тестиование для гостевой книги в теме ООП и в теме исключения для задачи 
***
# Задание №2
Задача two sum со списком порядка 10^5 

Импортировали функцию randint из модуля random для генерации целых чисел:
```python
$ from random import randint
```
Создали пустой список numbers и сгенирировали в него случайные целые числа от 10 до -10 :
```python
$ numbers = []
$ for i in range(10^6):
$    numbers.append(randint(-10, 10))
```
И запустили на выполнения две функции с данным списком:
```python
$ if __name__ == "__main__":
$    print(two_sum_brute(numbers, 9))
$    print(two_sum(numbers, 9))
```
Результат:
![alt text](https://github.com/nastyandreeva/Tasks/blob/master/2/Время.JPG)
