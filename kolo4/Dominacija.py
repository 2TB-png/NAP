def main():
    B = int(input())
    E = int(input())

    if B < E:
        print("sturka")
        return 0

    if B > E+3 or B > E*2:
        print("W")
        return 0

    print(min(E+4-B, E*2-B))
main()