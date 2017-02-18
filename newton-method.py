# simple program for solving a computer science homework (Newton method)
# f(x)  = (1/4)x^4 + (1/2)x^2 - x
# f'(x) = x^3 + x - 1
# f''(x) = 3x^2 + 1
# break condition: l^2 < e
# l^2   = (f'(x)^2 / f''(x))
# e = 10^-6

from math import pow


def first_derivation(x):
    result = pow(x, 3) + x - 1
    return result


def second_derivation(x):
    result = 3 * pow(x, 2) + 1
    return result


def calc_l(x):
    result = pow(first_derivation(x), 2) / second_derivation(x)
    return result


def iteration_step(x):
    x -= (first_derivation(x) / second_derivation(x))
    return x


def main():
    print "start"
    x = 2
    e = pow(10, -6)
    i = 0
    max_iterations = 10
    # test for break condition and max iteration steps
    while (calc_l(x) > e) and (i < max_iterations):
        x = iteration_step(x)
        print "x = " + str(x) + ",  i = " + str(i)
        i += 1
    print "end"
    # print break condition parameters
    print "l = " + str(calc_l(x)) + ",   e = " + str(e)


if __name__ == '__main__':
    main()
