# Q1:

def send_message(to, message="Hello", /, *attachments, urgent=False, **meta):
    print(f"To: {to}")
    print(f"Message: {message}")
    print(f"Attachments: {attachments}")
    print(f"Urgent: {urgent}")
    print(f"Metadata: {meta}")

send_message("Alice", "Hi", "file1.txt", "file2.png", urgent=True, sent_by="Josh", priority=1)

# To: Alice = (positional only)
# Message: Hi = (positional but optional)
# Attachments: (file1.txt, file2.png) = (positional, any number of args including 0)
# Urgent: True = (keyword only, since it comes AFTER the *args parameter)
# Metadata: {sent_by: Josh, priority: 1} = (any number of keyword only args seperated by key/value pairs in a **kwargs dict)

#Q2: 

def calculate_total(price=50, tax=0.1, discount=0.0, *, tip=0.15):
    return (price - discount) * (1 + tax + tip)

# The call below raises a TypeError:
calculate_total(price=100, discount=10, tip=0.2)

# The bug is tax=0.1, since it is a positional only you can not express it as a keyword argument in the function
# or alternatively you could move the / to just price and keep tax as a default
# To allow price to be a keyword as well you can set a default value and just remove the / entirely

#Q3:

def submit_report(daily, ops, /, *args, sent_by, encrypted, **kwargs):
    print(f'Daily: {daily}')
    print(f'Ops: {ops}')
    print(f'Args: {args}')
    print(f'Sent_by: {sent_by}')
    print(f'Encrypted: {encrypted}')
    print(f'Kwargs: {kwargs}')

submit_report("daily", "ops", "data.csv", sent_by="system", encrypted=True)
