def check_isbn():
    z1, z2, z3, z4, z5, z6, z7, z8, z9, z10 = 3, 5, 5, 1, 5, 5, 1, 6, 7, 7

    s = 1 * z1 + 2*z2 + 3*z3 + 4*z4 + 5*z5 + 6*z6 + 7*z7 + 8*z8 + 9 * z9

    if s % 11 == z10:
        return True
    else:
        return False