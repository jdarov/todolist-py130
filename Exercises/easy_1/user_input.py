def until_stop(prompt):
    while True:
        answer = input(prompt)

        if answer.lower() == 'stop':
            return
        yield answer


for answer in until_stop("Please enter a string('stop' to end): "):
    print(f"You said: {answer}")