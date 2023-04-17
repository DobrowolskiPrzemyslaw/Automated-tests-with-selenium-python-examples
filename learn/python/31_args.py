
def rzeczy(pierwszy_argument,*args):
    print(pierwszy_argument)
    print(args[0])
    for arg in args:
        print(arg)

rzeczy('malpa','koc','laptop')