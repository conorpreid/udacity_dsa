### Project 1 - Unscramble Computer Science Problems

This file describes the time complexity of each task that makes up this
project. BigO Notation is used throughout.

[Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt), and the [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation) wiki page are used as references.

##### Task 0
Time Complexity : *O(1)* \
Details : This script runs in *O(1)*, since we use a get operation on a list twice.
*Get Item* on lists is *O(1)*.

##### Task 1
Time Complexity : *O(n)* \
Details : We perform 4 *Add* operations on a set in this script, which
run in *O(1)*. But we also loop through two lists, so ultimatly this script
runs in *O(n)* where *n* is the larger of the number of records in
*calls* or *texts*.

##### Task 2
Time Complexity : *O(n)* \
Details : Again, this script involves looping though every item in *calls*, so
runs in *O(n)*. We perform a *store* operation each time, which runs in *O(1)*.

##### Task 3
Time Complexity : *O(n log n)* \
Details : Once again we loop through the contents of a list, which is *O(n)*.
We also sort the final list before printing, which is *O(n log n)*.

##### Task 4
Time Complexity : *O(n log n)* \
Details : Same as Task 3, we loop through a list which is *O(n)* but sort the
final resulting list which is *O(n log n)*
