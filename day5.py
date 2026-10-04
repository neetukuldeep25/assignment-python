# prime number
#  for num in range(2, 51):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

# Fibonacci Sequence
a = 0
b = 1
count = 0

while count < 10:
    print(a)
    a, b = b, a + b
    count += 1