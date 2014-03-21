Implementations of several different data structures in Python. For practice!

A Linked List with the following functions:
    insert(val): Add a node with the value = val at the head of the list
    pop(): Pop and return the item at the head of the list
    size(): Return the number of elements in the list
    remove(val): Remove from the list the first node with its value = val
    search(val): Return (but do not remove) the first node with its value = val

A stack with the following functions:
    push(val): Add a node with the value = val to the top of the stack
    pop(): Remove the item at the top of the stack and return it

A queue (as a double-linked list) with the following functions:
    enqueue(val): Add a node with the value = val to the head of the queue
    dequeue(): Remove the item at the tail of the queue and return it
    size(): Return the number of nodes in the queue

A hash table (a linked list of linked lists... defeating the purpose...) with the following functions:
    A constructor that takes as an argument the size of the hash table
    hash(key): Hashes the string key by its characters' ordinal values
    set(key, val): Puts the key, val pair into the hash table
    get(key): Gets the val paired with the key in the hash table

A make_month function for practicing hashing
    A factory function for generating an object of a given year and month
    With a day function that determines the day of the week of any given date
    Collaborated with one Steven Babineau on this here code

A binary search tree with the following functions:
    insert(val): Insert a value into the tree
    contains(val): Return a boolean indicating whether the val is in the tree
    size(): Return the size of the tree
    depth(): Return the depth of hte deepest leaf of the tree
    balance(): Return a value indicating how well the tree is balanced around the root
    in_order(): Return a generator that traverses the list in order
    pre_order(): Return a generator that traverses the list in a pre-order fashion
    post_order(): Return a generator that traverses the list in a post-order fashion
    breadth_first(): Return a generator that traverses the list in a breadth first fashion
    delete(val): Delete the val from the tree. If the val is not in the tree the function does nothing

An insertion sort function (Code translated from Wikipedia pseudo-code: http://en.wikipedia.org/wiki/Insertionsort).

A merge sort function (Code translated from Wikipedia pseudo-code: http://en.wikipedia.org/wiki/Mergesort).

A quick sort function (Code translated from Wikipedia pseudo-code: http://en.wikipedia.org/wiki/Quicksort).

A radix sort function

When the sort functions are called from the command line, they will print out a simple comparison between best and worst case scenarios of sorting a large number of integers.
With bonus analysis for pivot selection in the quick sort function (Sedgewick refers to Robert Sedgewick as mentioned in the Wikipedia article).

[![Build Status](https://travis-ci.org/markcharyk/data-structures.png?branch=master)](https://travis-ci.org/markcharyk/data-structures)
