def rev_int(n):
    n = str(n)
    if n[0] != "-":
        return n[::-1]
    elif n[0] == "-":
        return f"{n[0]}{n[:0:-1]}"
print(rev_int(-12345))