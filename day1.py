# write a program to sum of the numbers entered using for loop-
number_count=int(input("how many numbers to sum:"))
total_sum=0
for i in range(number_count):
    number=int(input(f"enter the number {i+1}:"))
    total_sum+=number
print("sum of the numbers are:",total_sum)