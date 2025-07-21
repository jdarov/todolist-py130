def combine(arg1, arg2, arg3, /):
    return (arg1, arg2, arg3)

print(combine(1, 'hello', None))

def multiply(num1, num2, /):
    return num1 * num2

def describe_pet(animal_type, /, *, name=''):
    return f'{name} is an animal of type {animal_type}'

print(describe_pet('squirrel'))
print(describe_pet('raccoon', name='john'))

def calculate_average(*args):

    return (sum(args) / len(args) if args else None)

def find_person(**kwargs):
    return next((f'{name} is a {profession}' for name,profession in kwargs.items() if name == 'Antonina'), 
                'Antonina not found')

print(find_person(John="Builder", Kitty='Hawk', Antonina='TA'))

def concat_strings(*args, sep=' '):
    return sep.join(args)

def register(username, /, age, *, password):
    return (f'username:{username}\n'
            f'age: {age}\n'
            f'password: {password}')

def print_message(*, message, level='INFO'):
    return f'{level} {message}'

print(print_message(message="hello"))