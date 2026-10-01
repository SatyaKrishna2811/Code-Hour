n = input()
if n in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    print("uppercase")
elif n in list("abcdefghijklmnopqrstuvwxyz"):
    print("lowercase")
elif n in list("0123456789"):
    print("digit")
elif n in list("!@#$%^&*()_+-=~`"):
    print("special")
