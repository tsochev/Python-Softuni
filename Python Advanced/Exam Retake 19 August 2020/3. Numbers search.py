def numbers_searching(*args):
    duplicates = []
    missing_el = ""
    max_el = max(args)
    min_el = min(args)
    for el in range(min_el, max_el):
        if el not in args:
            missing_el = el
    uniq = set([x for x in args if args.count(x) > 1])
    duplicates.append(missing_el)
    duplicates.append(sorted(list(uniq)))

    return duplicates


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
