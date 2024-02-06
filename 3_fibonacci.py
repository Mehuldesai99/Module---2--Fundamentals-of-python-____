# >>> 3.  Write a Python program to get the Fibonacci series of given range.

n = int(input("Enter a range : "))
f_series = [0, 1]
while len(f_series) < n:
    next_num = f_series[-1] + f_series[-2]
    f_series.append(next_num)
print("Fibonacci series : ",f_series)







