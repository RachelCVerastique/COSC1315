#
# decimal = float(input("enter decimal: "))
#
# print(f"\n you entered {format(decimal, '.2f')}")
#
# print("\nyou entered ", format(decimal, '.2f'))

# def main():
#     firstAge = int(input('Enter your age: '))
#     secondAge = int(input('Enter your best friends age:'))
#     total = sum(firstAge, secondAge)
#     print(f'Together you are {total} years old')
#
# def sum(num1, num2):
#     result = num1 + num2
#     return result
#
# main()

color = ['red','blue','orange','pink']
print(*color, sep=", ")
print()
print(*color, sep="\n")
