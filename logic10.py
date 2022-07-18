def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return int(a)==a and (a//10)>0 or (a//10)<0

x=main(36)

print(x)
