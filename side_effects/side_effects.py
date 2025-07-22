bar = 42
qux = [1, 2, 3]
baz = 3

def foo(lst):
    value = lst.pop()
    print(f'popped {value} from the list')
    return value + bar + baz

foo(qux)
#mutates a list outside of the function qux (removes the last element)
#outputs to the screen
