
def draw_1d(n, char):
    print(char*n)
##
##
##c1= "*"
##c2= "*"
##c3= "*"
##c4= "*"
##c5= "*"
##draw_1d(10, c1)
##draw_1d(10, c2)
##draw_1d(10, c3)
##draw_1d(10, c4)
##draw_1d(10, c5)


def draw_2d(n, m ,char):
    # n - numbers of characters in 1 row
    # m - number of rows
    # char - character to be repeated
    for number in range(m):
        print(n*char)
