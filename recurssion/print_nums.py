#f(5) will first print then calls f(4)
def print_fun(n):

    if n==0:
        return
    else:
        print(n)
        print_fun(n - 1)

# print_fun(5)

#f(5) will wait for the f(4) to finsh to print, f(4) will wait for f(3) to finish and so on

def fun_print(n):
    if n==0:
        return
    else:
        fun_print(n - 1)
        print(n)
# fun_print(5)


def fun_print2(n):
    if n==0:
        return
    else:
        print(n)
        fun_print2(n - 1)
        print(n)
fun_print2(5)
