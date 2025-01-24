"""
Two ways to run this file:

% python changing_psygnal.py

% pytest changing_psygnal.py

"""

from psygnal import Signal
import pytest

class MyObject:
    # define one or signals as class attributes
    value_changed = Signal(str)

# create an instance
my_obj = MyObject()

# You (or others) can connect callbacks to your signals
@my_obj.value_changed.connect
def on_change(new_value: str):
    print(f'Hi {new_value}!') # prints the new string - Hi {new_value}
    my_obj.new_value = new_value

def get_name_and_say_hello():
    my_input = input("enter a name here: ")
    my_obj.value_changed.emit(str(my_input))
    return my_obj.new_value


if __name__ == "__main__":
    count = 0
    while count < 5:
        name = get_name_and_say_hello()
        print(f"Said Hi to.... {name}")
        count = count + 1

""" TEST """
def test_say_hello(monkeypatch):
    names = ['Sally', 'Bob', 'Harriet', 'Bart', 'Erica']
    count = 0
    while count < 5:
        monkeypatch.setattr('builtins.input', lambda _: names[count])
        result = get_name_and_say_hello()
        assert result == names[count]
        count = count + 1

