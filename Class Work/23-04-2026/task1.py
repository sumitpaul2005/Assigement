# File Handelling

# try:
#     n = int(input("Enter the number : "))
#     print(n)
# except ValueError as e:
#     print(e)

# try:
#     n = int(input("Enter the number : "))
#     n2 = int(input("Enter the number : "))
#     print("Division : ",n/n2)
# except ZeroDivisionError as e:
#     print(e)

try:
    l = [10,20,621,42,6,2]
    n = int(input("Enter the number : "))
    print("Index : ",l[n])
# except IndexError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except:
#     print("Error")
except Exception as e: #It will shows all type of error
    print(e)