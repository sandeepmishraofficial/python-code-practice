
# #print 1 to 4 numbers
# # for i in range(1,5):
# #     print(i, end=" ")

# =============================================================================================

# # write the program in leap year

# print("leap Year fron 1900-2025 are: ")
# for i in range(1900,2025):
#     if(i%4==0):
#         print(i,end=" ")


# <===================================================================================================>

# write a program to genrate calender of a month given the start_day and the number  of day in that month

# startDay = int(input("Enter the start day of month(1-7) : "))
# num_of_days = int(input("Enter number of Day : "))
# print("Monday  Tuesday Webnesday Thursday Saturday Sunday  ")
# print("-------------------------------------------")

# for i in range(startDay-1):
#     print(end="         ")
# i = startDay-1
# for j in range(1,num_of_days+1):
#     if(i>6):
#         print()
#         i = 1
#     else:
#         i = i+1
#         print(str(j)+" ", end=" ")



# ===================================================================================================================
# write the program to print the pattern

# for i in range(5):
#     print()
#     for j in range(5):
#       print("*", end=" ")


# =====================================================================================================

# pattern question

# for i in range(1,6):
#     print()
#     for j in range(i):
#         print("*", end=" ")


# ==========================================================================================
# print pattern

# for i in range(1,6):
#     print()
#     for j in range(0,i+1):
#         print(j, end =" ")


# ===========================================================================================
#  Generate calender

# import calendar
# y = int(input("Enter the year: "))
# m = 1
# print("\n********** CALENDER **********")
# Cal = calendar.TextCalendar(calendar.SUNDAY)
# i=1
# while i<=12:
#     Cal.prmonth(y,i)
#     i+=1

# ==========================================================================================
# factorial number 

# num = int(input("Enter the number: "))
# if(num==0):
#     fact = 1
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print("Factorial of",num,"is",fact)

# ===============================================================================================
# write the prime and composite

# number = int(input("Enter the Number: "))
# iscomposite = 0
# for i in range(2,number):
#     if(number%i==0):
#         iscomposite =  1
#         break
# if(iscomposite ==1):
#     print("number is composite")
# else:
#     print("number is prime")

# =========================================================================================================
# the pass statement 

for i in "HELLO":
    pass
    print("pass :",i)
print("Done")

