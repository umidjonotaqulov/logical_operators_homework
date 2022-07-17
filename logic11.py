def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a//100)*100+((a//10)%10)*10+a%10==a

x=main(345)

print(x)
