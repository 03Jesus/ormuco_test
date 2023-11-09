# Question A
"""
write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis
and returns whether they overlap.
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
"""


def overlap(x1, x2, x3, x4):
    return (x1 <= x4 and x2 >= x3) or (x3 <= x2 and x4 >= x1)


if __name__ == "__main__":
    s_line1 = float(input("Enter the start of line 1: "))
    e_line1 = float(input("Enter the end of line 1: "))
    s_line2 = float(input("Enter the start of line 2: "))
    e_line2 = float(input("Enter the end of line 2: "))
    if overlap(s_line1, e_line1, s_line2, e_line2):
        print(
            f"The lines ({s_line1}, {e_line1}) and ({s_line2}, {e_line2}) overlap.")
    else:
        print(
            f"The lines ({s_line1}, {e_line1}) and ({s_line2}, {e_line2}) do not overlap.")
