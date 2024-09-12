def string_functions(s):
    length = len(s)
    upper_case = s.upper()
    lower_case = s.lower()
    return length, upper_case, lower_case

input_string = "Hello World"
length, upper, lower = string_functions(input_string)
print(f"Length: {length}, Upper: {upper}, Lower: {lower}")
