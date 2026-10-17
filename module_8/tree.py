import turtle

MIN_BRANCH_LEN = 5
BRANCH_DELTA = 15


def tree(branch_len, t):
    if branch_len > MIN_BRANCH_LEN:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - BRANCH_DELTA, t)
        t.left(40)
        tree(branch_len - BRANCH_DELTA, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100, t)
    t.speed(5)
    my_win.exitonclick()

main()
