def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (int(a)//10000)>0 or (int(a)//10000)<0

x=main(54321)

print(x)
