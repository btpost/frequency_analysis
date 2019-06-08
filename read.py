
def reader(args):
    if args[0] == '-s':
        return args[1]
    else:
        return open(args[0]).read()