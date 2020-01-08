n = 3
i= 1
list = []
while i <= n:
    if (i % 3 == 0 and i % 5 == 0):
        list.append("FizzBuzz")
    elif(i % 5 == 0):
        list.append("Buzz")
    elif(i % 3 == 0):
        list.append("Fizz")
    else:
        list.append(i)
    i = i + 1

for i in list:
    print(i)
