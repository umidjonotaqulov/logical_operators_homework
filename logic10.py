def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return int(a)==a and (a//10)*10+(a%10)==a

x=main(int(34))

print(x)
