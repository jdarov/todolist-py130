def generator_function():

    for num in range(1, 6):
        yield num

for num in generator_function():
    print(num)



