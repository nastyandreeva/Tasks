import pytest
from main import funct

def test_one():
  assert  funct(9, 'oct') == 'Девять', '0o11'

def test_two():
  assert  funct(5, 'bin') == 'Шесть', '0b101' 

def test_three():
  assert  funct(10, 'bin') == 'Число не входит в указанный интервал'
