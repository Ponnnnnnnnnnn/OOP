def pattern1(n, i=1):
    if i <= n:
        print('*' * i)
        pattern1(n, i + 1)

def pattern2(n, i=None):
    if i is None:
        i = n
    if i > 0:
        print('*' * i)
        pattern2(n, i - 1)

def pattern3(n, i=1):
    if i <= n:
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))
        pattern3(n, i + 1)

def pattern4(n, i=None):
    if i is None:
        i = n
    if i > 0:
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))
        pattern4(n, i - 1)

def pattern5(n, i=1):
    if i <= n:
        print(' ' * (n - i), end='')
        print('*' * i)
        pattern5(n, i + 1)

def pattern6(n, i=None):
    if i is None:
        i = n
    if i > 0:
        print(' ' * (n - i), end='')
        print('*' * i)
        pattern6(n, i - 1)

# Input value of 'a'
a = int(input())

# Call each recursive function for the respective pattern
pattern1(a)
print()
pattern2(a)
print()
pattern3(a)
print()
pattern4(a)
print()
pattern5(a)
print()
pattern6(a)
print()
