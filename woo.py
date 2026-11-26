def count_down(n):
    if n <= 0:
        print("Countdown finished!")
        return
    print(n)
    m = n-1
    count_down(m) # count_down callback

count_down(5)

def print_start(num):
    if num > 0:
        print_start(num-1) # print_start
        print("*"*num  )

print_start(5)

def gugu(dan, num=1):

    print("%d x %d = %d" % (dan, num, dan*num))
    if num < 9:
        gugu(dan, num + 1) # gugu callback

for i in range(2, 10):
    gugu(i)


def pow(base, exponent):
    if exponent == 0:
        return 1
    else:
        print("base:", base, "exponent:", exponent)
        return base * pow(base, exponent - 1) # pow callback

print(pow(2, 4))

# #########################

def arr_sum(arr, n):
    if n <= 0:
        return 0
    else:
        return arr[n - 1] + arr_sum(arr, n - 1) # arr_xum callback

foo = [1, 2, 3, 4, 5]
arr_sum(foo, len(foo))
#########################

def fibocacci(n):
    if n <= 1:
        return 0
    else:
        return fibocacci(n - 1) + fibocacci(n - 2) # fibonacci callback

print(fibocacci(5))
    

