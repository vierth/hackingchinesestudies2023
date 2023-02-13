# defining functions allows us to easily reuse code
def greeting(name):
    print(f"hello {name}, everyone! hope your day is lovely")

# greeting with multiple paramaters
def complex_greeting(name, counterpart_name):
    print(f"hello {name}, everyone! hope your day is lovely. my name is {counterpart_name}")

def complex_greeting_with_keyword(name, counterpart_name="Jim"):
    print(f"hello {name}, everyone! hope your day is lovely. my name is {counterpart_name}")

greeting("Prof V")
complex_greeting("Prof V", "Paul")
complex_greeting_with_keyword("Prof V")
complex_greeting_with_keyword("Prof V", "Tim")
complex_greeting_with_keyword("Prof V")