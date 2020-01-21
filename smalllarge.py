largest = -1
smallest = None


while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try:
        val = int(num)
    except:
        print('Invalid input')
        continue

    if smallest is None:
        smallest = val
    if val > largest:
        largest = val
    elif val < smallest:
        smallest = val

print("Maximum is", largest)
print("Minimum is", smallest)
