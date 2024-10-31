def perfect(num):
    a = [i for i in range(1,num) if num % i ==0]
    return sum(a) == num
perfect_numbers = [num for num in range(1,1000000) if perfect(num)]
print("Perfect numbers less than 1000000:", perfect_numbers)