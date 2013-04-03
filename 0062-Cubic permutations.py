def main():
    table = {}
    val = {}
    start = 345
    while True:
        key = ''.join(sorted(str(start**3)))
        try:
            table[key] += 1
            if val[key]:pass
        except KeyError:
            table[key] = 1
            val[key] = start**3
        if table[key] == 5:
            print val[key]
            break
        start += 1
if __name__ == '__main__':
    main()
