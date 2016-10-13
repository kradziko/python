def fib(n):
    i ,a ,b= 1,0,1
    while (i <= n):
        print "F%-2i = %-3i" % (i, b)
        b +=a
        a = b-a
        i+=1

fib(10)
