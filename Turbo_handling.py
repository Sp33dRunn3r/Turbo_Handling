# Error Handling
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
            age = print('Please enter a number ')
    except ZeroDivisionError:
            age = print('Please enter a number higher than 0')
    else:
        print('Thank you!')
        break

# Error Handling
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
            age = print('Please enter a number ')
            continue
    except ZeroDivisionError:
            age = print('Please enter a number higher than 0')
    else:
        print('Thank you!')
        break
    finally:
        print('ok, I am finally done')
