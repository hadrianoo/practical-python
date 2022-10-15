# bounce.py
#
# Exercise 1.5


height = 100
b = 3 / 5
bounce = 1
for _ in range(10):
    height = height * b
    print(bounce, round(height, 4))
    bounce += 1


