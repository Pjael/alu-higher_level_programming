#!/usr/bin/python3
def print_arg(argv):
    i = len(argv) -1
    if i == 0:
        print('{:d} arguments.'.format(i))
        return
    else:
        if i == 1:
            print('{:d} argument:'.format(i))
        else:
            print('{:d} arguments:'.format(i))
        p = 1
        while p <= i:
            print('{:d}: {:s}'.format(p, argv[p]))
            p += 1

if __name__ == '__main__':
    import sys
    print_arg(sys.argv)
