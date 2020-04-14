count = 1
print(count)

while (count <= 150):
    fizz = count / 3
    buzz = count / 5

    if (float(fizz).is_integer() and not float(buzz).is_integer()):
        print("fizz")
    elif (float(buzz).is_integer() and not float(fizz).is_integer()):
        print("buzz")
    elif (float(buzz).is_integer() and float(fizz).is_integer()):
        print("fizzbuzz")
    else:
        print(count)

    count += 1

# Not elegant but gets the job done
