def show_fibonacci(count):
    first = 0
    second = 1

    for i in range(count):
        print(first, end=' ')
        next_num = first + second
        first = second
        second = next_num

#main
n = int(input("how many numbers? "))
show_fibonacci(n)
