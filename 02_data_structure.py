l = [i**2 for i in range(5)]
print(*l)
m = [[i * 10 + j for j in range(5)] for i in range(5)]
print(*m)


# tuple
t = 1, "a", 1.5
print(t)
# error
# t[1] = 1


# dictionary
d = {"a": 1, "b": 2, "c": 3}
print(d["a"])
for x in d.items():
    print(x)


# set
a = set()
a.add(1)
a.add(2)
a.add(2)
print(a)
b = {2, 3, 4, 3}
print(b)
print(a & b) # 積
print(a | b) # 和
