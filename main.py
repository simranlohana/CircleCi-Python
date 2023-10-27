def to_upper(name):
    return name.upper()

def say_hello(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}') # Press F8 to toggle the breakpoint.
    
# Press the green button in the gutter to run the scipt
if __name__ == '__main__':
    name = 'simran'
    say_hello(name)
    up = to_upper(name)
    print(up)