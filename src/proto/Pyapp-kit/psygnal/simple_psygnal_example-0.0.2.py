#!/usr/bin/env -S python -u

"""
The observer pattern is a software design pattern in which
an object maintains a list of its dependents ("observers"), 
and notifies them of any state changes – usually by calling
a callback function provided by the observer.

This file is a simple example of using psygnal, slightly
modified from: https://psygnal.readthedocs.io/en/latest/

"""

from psygnal import Signal

class MyObject:
    # define one or signals as class attributes
    value_changed = Signal(str)

    def __init__(self, value=0):
        self._value = value

    def set_value(self, value):
        if value != self._value:
            self._value = str(value)
            # emit the signal
            self.value_changed.emit(self._value)


# create an instance
my_obj = MyObject()

# You (or others) can connect callbacks to your signals
@my_obj.value_changed.connect
def on_change(new_value: str):
    print(f'"{new_value}!"')

def curious():
    print("Sent by", Signal.sender())
    assert Signal.sender() == my_obj


count = 0
my_input = ""
while count < 5:
    my_input = input("enter a name here: ")
    # The object may now emit signals when appropriate,
    # (for example in a setter method)
   
    # my_obj.value_changed.connect(curious)
    my_obj.value_changed.emit('Hi ' + str(my_input))  # prints the new string "Hi {new_value}"
    count = count + 1    

# The object may now emit signals when appropriate,
# (for example in a setter method)
# my_obj.value_changed.emit('hi')  # prints "The value changed to hi!"
