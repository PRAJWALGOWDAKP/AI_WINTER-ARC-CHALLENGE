def add(*args):
    print(args)
    return sum(args)
res=add(10,20,30,40)
print(res)

print()

def num(*args):
    for num in args:
        print(num)
num(10,20,30,40)

print()

def details(**kwargs):
    print(kwargs)
details(name="Prajwal",age=23,city="Banglore")

print()

def info(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")

info(name="Prajwal",age=23,city="Banglore")

print()

def merge(*args,**kwargs):
    print(args)
    print(kwargs)

merge(10,20,30,40,name="Prajwal",age=23,city="Banglore")

    