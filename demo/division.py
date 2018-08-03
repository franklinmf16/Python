print('Give me two numbers, and I\'ll divide them')
while True:
    first = input("\nFirst number: ")
    if first == 'q':
        break
    second = input("\nSecond number: ")
    try:
        if second == 'q':
            break       
        answer = int(first) / int(second)
    except ZeroDivisionError: 
        print("you can't divide by 0!")
    else:
        print(answer)
