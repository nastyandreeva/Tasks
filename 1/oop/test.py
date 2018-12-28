import pytest
from main import *

def test_dict():
  new_dict={"f_name":Настя,"s_name":Андреева,"email":nastyandreeva7@gmail.com, "birthyear":1998, "country":Россия, "city":Санкт-Петербруг}
  with pytest.raises(KeyError):
        new_dict.get('middle_name')

@pytest.mark.parametrize()
