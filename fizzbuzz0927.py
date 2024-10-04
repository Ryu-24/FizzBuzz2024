i=0
a = int(input("数字を入力してください"))
while(i < a):
    i += 1
    print(i)
    if(i % 15 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")

    elif(i % 5 == 0):
        print("Buzz")