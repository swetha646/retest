#prime number 

# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Number is not prime")
# else:
#     for i in range(2, int(num ** 0.5) +1):
#         if num % i == 0:
#             print("Number is not prime")
#             break
#     else:
#         print("Number is a prime number")

#reverse a list

# nums =[10,20,30,40,50]
# start = 0
# end = len(nums) - 1
# for i in nums:
#     if start < end:
#         nums[start],nums[end] = nums[end],nums[start]
#         start +=1
#         end -=1
# print(nums)

#pattern printing

# n = 7
# for i in range(1, n+1):
#     for j in range(n - i):
#         print(" ",end = "")
#     for k in range(2 *i -1):
#         print("*",end ="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n -i):
#         print(" ",end ="")
#     for k in range( 2 *i -1):
#         print("*",end="")
#     print()