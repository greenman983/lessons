from operator import truediv

immutable_var = 1, 5, "vova", 1.6
print(immutable_var)
# immutable_var [3] = "fedor"
# print(immutable_var)
# tuple - неизменяемый объект
mutable_var = [1, 2, "senya", "dima"]
print(mutable_var)
mutable_var [1] = ["givi", "gogi"]
print(mutable_var)
