# 1. Variable Declaration and Types
a = 15
b = 12

print(type(a))
print(type(b))

# 2. Basic Arithmetic Operations
# Addition
result = a + b
print("Addition:", result)

# Subtraction
result = a - b
print("Subtraction:", result)

# Multiplication
result = a * b
print("Multiplication:", result)

# Division
result = a / b
print("Division:", result)


# 3. Using Variables and Type Casting
c = int(a / b)
print("Integer value of c:", c, "Type:", type(c))

c = float(c)
print("Float value of c:", c, "Type:", type(c))

# 4. Working with Strings
message = "The result of a divided by b is: "
result_str = str(c)
print(message + result_str)

# 5. Using Comparison Operators
print("a > b:", a > b)
print("a == b:", a == b)
