def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (int(a)//10)>0 or (int(a)//10)<0

x=main(600)

print(x)
