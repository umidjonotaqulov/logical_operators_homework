def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (int(a)//10)>0 and (int(a)//10)<0

x=main(3)

print(x)
 