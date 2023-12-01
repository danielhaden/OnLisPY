
def double(x):
    return 2 * x

print(double(1))

print(lambda x: x * 2)

## no separate namespace

def function_and_variable_name():
    double = 5

    double(double)

## Functional arguments