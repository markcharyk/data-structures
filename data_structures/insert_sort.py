def insertion_sort(unsorted):
    for i in range(1, len(unsorted)):
        current = unsorted[i]
        comp = i
        while comp > 0 and unsorted[comp - 1] > current:
            unsorted[comp] = unsorted[comp - 1]
            comp -= 1
        unsorted[comp] = current
    return unsorted


if __name__ == '__main__':
    best_case, worst_case = [], []
    for i in xrange(16384):
        best_case.append(i)
        worst_case.append(16383 - i)
    import time
    t1 = time.time()
    insertion_sort(best_case)
    t2 = time.time()
    print "Best case: %f seconds" % (t2 - t1)
    t3 = time.time()
    insertion_sort(worst_case)
    t4 = time.time()
    print "Worst case: %f seconds" % (t4 - t3)
