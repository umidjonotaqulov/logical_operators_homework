def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (int(a)//100)>0 or (int(a)//100)<0

x=main(345)

print(x)
