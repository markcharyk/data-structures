import random


def quick_sort(unsorted, pivot_select=None):
    if len(unsorted) <= 1:
        return unsorted
    pivot = select_pivot(unsorted, pivot_select)
    less, greater = [], []
    for elem in unsorted:
        if elem < pivot:
            less.append(elem)
        else:
            greater.append(elem)
    result = quick_sort(less, pivot_select)
    result.append(pivot)
    result.extend(quick_sort(greater, pivot_select))
    return result


def select_pivot(lst, selector):
    if selector == 'random':
        return lst.pop(random.randint(0, len(lst) - 1))
    elif selector == 'middle':
        return lst.pop(len(lst) // 2)
    elif selector == 'median':
        candidates = [lst[0], lst[len(lst) // 2], lst[-1]]
        result = quick_sort(candidates)[1]
        lst.remove(result)
        return result
    else:
        try:
            return lst.pop(selector)
        except:
            return lst.pop(0)


if __name__ == '__main__':
    best_case, worst_case = [], []
    for i in xrange(750):
        best_case.append(i)
        worst_case.append(i)
    import time
    t1 = time.time()
    quick_sort(best_case, 'middle')
    t2 = time.time()
    print "Best case: %f seconds" % (t2 - t1)
    t1 = time.time()
    quick_sort(worst_case)
    t2 = time.time()
    print "Worst case: %f seconds" % (t2 - t1)

    print "\nPivot Selection Comparisons:\n"
    random.shuffle(best_case)
    control = best_case
    selector = {
        None: 'the first item as the',
        -1: 'the last item as the',
        'random': 'a random',
        'middle': 'the middle item as the',
        'median': 'the Sedgewick method for determining the'
    }
    for k, v in selector.iteritems():
        unsorted = control
        t1 = time.time()
        quick_sort(unsorted)
        t2 = time.time()
        print "For %s pivot: %f" % (v, t2 - t1)
