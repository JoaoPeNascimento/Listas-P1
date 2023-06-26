n1 = input()
p1 = int(input())
n2 = input()
p2 = int(input())
n3 = input()
p3 = int(input())

if p1 > p2 and p1 > p3 and p2 > p3:
    print('{} {}'.format(n3, p3))
    print('{} {}'.format(n2, p2))
    print('{} {}'.format(n1, p1))

if p1 > p2 and p1 > p3 and p3 > p2:
    print('{} {}'.format(n2, p2))
    print('{} {}'.format(n3, p3))
    print('{} {}'.format(n1, p1))

if p2 > p1 and p2 > p3 and p1 > p3:
    print('{} {}'.format(n3, p3))
    print('{} {}'.format(n1, p1))
    print('{} {}'.format(n2, p2))

if p2 > p1 and p2 > p3 and p3 > p1:
    print('{} {}'.format(n1, p1))
    print('{} {}'.format(n3, p3))
    print('{} {}'.format(n2, p2))

if p3 > p1 and p3 > p2 and p1 > p2:
    print('{} {}'.format(n2, p2))
    print('{} {}'.format(n1, p1))
    print('{} {}'.format(n3, p3))

if p3 > p1 and p3 > p2 and p2 > p1:
    print('{} {}'.format(n1, p1))
    print('{} {}'.format(n2, p2))
    print('{} {}'.format(n3, p3))

if p1 == p2 and p1 > p3:
    if n2 > n1:
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n1, p1))
    elif n1 > n2:
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n1, p1))

if p1 == p2 and p1 < p3:
    if n2 > n1:
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n3, p3))
    elif n1 > n2:
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n3, p3))

if p1 == p3 and p1 > p2:
    if n1 > n3:
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n1, p1))
    elif n3 > n1:
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n3, p3))

if p1 == p3 and p1 < p2:
    if n1 > n3:
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n2, p2))
    elif n3 > n1:
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n2, p2))

if p2 == p3 and p2 < p1:
    if n2 > n3:
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n1, p1))
    elif n3 > n2:
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n1, p1))

if p2 == p3 and p2 > p1:
    if n2 > n3:
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n2, p2))
    elif n3 > n2:
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n3, p3))

if p1 == p2 and p2 == p3:
    if n1 > n2 > n3:
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n1, p1))
    elif n1 > n3 > n2:
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n1, p1))
    elif n2 > n1 > n3:
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n2, p2))
    elif n2 > n3 > n1:
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n3, p3))
        print('{} {}'.format(n2, p2))
    elif n3 > n1 > n2:
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n3, p3))
    elif n3 > n2 > n1:
        print('{} {}'.format(n1, p1))
        print('{} {}'.format(n2, p2))
        print('{} {}'.format(n3, p3))