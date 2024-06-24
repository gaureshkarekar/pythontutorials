


class MyCustomError(Exception):
    """Exception raised for custom error conditions."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def example_function(x):
    if x < 0:
        raise MyCustomError("Negative value not allowed")
    else:
        return x ** 2

try:
    result = example_function(-5)
except MyCustomError as e:
    print(f"An error occurred: {e}")


#  Urmila's error

class UrmilaError(Exception):
    def __init__(self,msg) :
        self.msg = msg
        super().__init__(self.msg)

def urmilaFunction():
    raise UrmilaError("Hello This is Urmila's error")

try:
    urmilaFunction()
except UrmilaError as ue:
    print(f"Custom created error occurred as {ue}")




