def string_operations(s):
    print(f"Original String: {s}")
    print(f"Length of String: {len(s)}")
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    print(f"Does string contain 'world': {'world' in s}")
    print(f"Replace 'world' with 'Python': {s.replace('world', 'Python')}")

if __name__ == "__main__":
    text = "Hello, world!"
    string_operations(text)
