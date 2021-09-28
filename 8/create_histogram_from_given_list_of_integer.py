def histogram(items):
    for n in items:
        output = ''
        times = n
        while (times>0):
            output +='s '
            times = times - 1
            print(output)
histogram([5])