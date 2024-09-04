
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

for i in range(1,6):
    print()
    for j in range(i):
        print("*", end=" ")