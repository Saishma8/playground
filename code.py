#function to get maximum from a list of nos
def maximum():
    y = raw_input("Enter your list:")
    x = y.split()
    try:
        highest = float(x[0])
        for i in x:
            if float(i) >= highest:
                highest = float(i)
    except:
        highest = x[0]
        for i in x:
            if i >= highest:
                highest = i
    print "The maximum of given list is", highest
    return highest

#function to get minimum from a list
def minimum():
    y = raw_input("Enter your list:")
    x = y.split()
    try:
        lowest = float(x[0])
        for i in x:
            if float(i) <= lowest:
                lowest = float(i)
    except:
        lowest = x[0]
        for i in x:
            if i <= lowest:
                lowest = i
    print "The minimum of given list is", lowest
    return lowest

#function to find sum of nos
def total():
    y = raw_input("Enter a list of numbers:")
    x = y.split()
    total = 0
    for i in x:
        total = total + float(i)
    print "The sum of given numbers is", total
    return total

#function to find average of nos
def mean():
    y = raw_input("Enter a list of numbers:")
    x = y.split()
    total = 0
    count = 0
    for i in x:
        total = total + float(i)
        count = count + 1
    print "The average of given numbers is", total/count
    return total/count


#Program code
action = raw_input("Enter the action to be performed: 'Max' 'Min' 'Sum' 'Avg' :")

if action == "Max":
    maximum()
elif action == "Min":
    minimum()
elif action == "Sum":
    total()
elif action == "Avg":
    mean()
else:
    print "Invalid input. Please try again"

# code to calculate sum of nos in a file
# sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_272363.txt').read())])
