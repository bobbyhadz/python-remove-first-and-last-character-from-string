# Remove first and last characters from a String in Python

my_str = 'apple'

# ✅ Remove the first and last characters from a string
result_1 = my_str[1:-1]
print(result_1)  # 👉️ 'ppl'

# ✅ Remove the first character from a string
result_2 = my_str[1:]
print(result_2)  # 👉️ 'pple'

# ✅ Remove the last character from a string
result_3 = my_str[:-1]
print(result_3)  # 👉️ 'appl'