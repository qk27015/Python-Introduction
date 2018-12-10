print("Hello World !")

# comment

print(3/2)
print(3//2)
print(2**3)

a = "abcdefghi"
print(len(a))
print(a[:]) # all
print(a[:-1])
print(a[3:-1])

a = 1
b = 2
print(float(a))
print(str(a) + str(b))
print("=====")

for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
