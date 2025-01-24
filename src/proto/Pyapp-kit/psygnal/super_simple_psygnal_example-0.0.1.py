from psygnal import Signal

class MyObject:
    # define one or signals as class attributes
    value_changed = Signal(str)

# create an instance
my_obj = MyObject()

# You (or others) can connect callbacks to your signals
@my_obj.value_changed.connect
def on_change(new_value: str):
    print(f'Hi {new_value}!') # prints the new string - Hi {new_value}

# Mock event loop to see the effect of new signals with 
# new values - watch the signal handler handle the changing values
count = 0
my_input = ""
while count < 5:
    my_input = input("enter a name here: ")

    # The object may now emit signals when appropriate,
    # (for example in a setter method)
    my_obj.value_changed.emit(str(my_input))
    count = count + 1
