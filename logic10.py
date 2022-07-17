def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a%10>0 and a//10>0 and int(a)==a

x=main(34)

print(x)
