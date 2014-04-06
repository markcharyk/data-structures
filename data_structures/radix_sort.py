import math


def radix_sort(unsorted, base=10):
    """Sorts some numbers using a radix sorting algorithms"""
    if not unsorted:
        return []
    # Determine the maximum size
    highest = int(math.log(max(unsorted), base)) + 1
    result = unsorted
    for i in xrange(1, highest+1):
        # Build the right number of buckets
        buckets = [[] for x in range(base)]
        # Bucket-ize the list
        for j in result:
            digit = j % (base ** i) // (base ** (i-1))
            buckets[digit].append(j)
        # Move the items from the buckets to a result list
        result = [item for bucket in buckets for item in bucket]
    return result


if __name__ == '__main__':
    print """Turns out there is no difference between best and worst cases
    because the radix sort will hit every number just as often no matter what"""
