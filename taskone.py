def magic(sub, s):
    # this performs the operation to check if substring can be formed using the given string of letters
    count = 0
    x = 0
    m = len(sub)
    while (x < m):
        n = sub[x] in s
        if (n == False):
            count = count + 1
        x = x + 1

    if (count != 0):
        print("false")
    else:
        print("true")


s = input("enter the string :")
sub = input("enter the substring:")
# calling function by passin string as parameters
magic(sub, s)