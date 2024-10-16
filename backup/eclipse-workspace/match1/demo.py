def process_user(user):
    match user:
        case {"name": name, "age": age}:
            return f"User {name} is {age} years old."
        case {"name": name}:
            return f"User {name} has an unknown age."
        case _:
            return "Unknown user"

# Testing
print(process_user({"name": "Alice", "age": 30}))  # Output: User Alice is 30 years old.
print(process_user({"name": "Bob"}))               # Output: User Bob has an unknown age.
print(process_user({"id": 123}))                   # Output: Unknown user
