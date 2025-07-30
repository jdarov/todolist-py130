from functools import partial

def format_message(sender, recipient, message):
    return f"From: {sender} To: {recipient} — {message}"

# Create a partial function called 'email_from_alice' that always sends from Alice
email_from_alice = partial(format_message, 'Alice')

print(email_from_alice("Bob", "Lunch at noon?"))


def order_coffee(size, milk, sugar):
    return f"{size} coffee with {milk} milk and {sugar} sugar."

# FIX the milk to always be 'oat'
coffee_with_oat_milk = partial(order_coffee, milk="oat")
coffer_large_oat = partial(order_coffee, 'Large', 'oat')

print(coffee_with_oat_milk("Large", sugar=1))
print(coffer_large_oat(1))
