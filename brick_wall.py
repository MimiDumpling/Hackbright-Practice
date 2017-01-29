from time import sleep

bricks = [ "[]", "[__]", "[____]", "[______]" ]

# my small wall
# [__][__][] ( 2 + 2 + 1)
# [____][__] (3 + 2)   
# [______][] (4 + 1)
# [____][__] (3 + 2)
# [__][__][] (2 + 2 + 1)


def row1(brick_size1, brick_size2):
    brick1 = brick_size1 # example code
    brick2 = brick_size2  # example code
    row1 = (brick2 + brick2 + brick1) # sample code, you can replace it
    return row1

def row2(brick_size2, brick_size3):
    brick1 = brick_size3 
    brick2 =  brick_size2 
    row2 = brick1 + brick2
    return row2

def row3(brick_size1, brick_size4):
    brick1 = brick_size4
    brick2 = brick_size1
    row3 = brick1 + brick2
    return row3


def row4(brick_size2, brick_size3):
    brick1 = brick_size3
    brick2 = brick_size2
    row4 = brick1 + brick2
    return row4

def row5(brick_size1, brick_size2):
    brick1 = brick_size1
    brick2 = brick_size2
    row5 = (brick2 + brick2 + brick1)
    return row5



def small_wall():
    """
    example of output of small wall. Note how the seams between the bricks
    meet at in the middle of another brick.
    [__][__][]
    [][__][__]
    [__][__][]
    [][__][__]
    [__][__][]
    """

    print row1(bricks[0], bricks[1])
    sleep(1)
    print row2(bricks[1], bricks[2])
    sleep(1)
    print row3(bricks[0], bricks[3])
    sleep(1)
    print row4(bricks[1], bricks[2])
    sleep(1)
    print row5(bricks[0], bricks[1])

small_wall()