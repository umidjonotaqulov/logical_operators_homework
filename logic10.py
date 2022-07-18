def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return 99>int(a)>10 or -99<int(a)<-10

x=main(95)

print(x)
