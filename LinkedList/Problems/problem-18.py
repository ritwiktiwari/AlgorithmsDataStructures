"""
Partition linked list on the basis of pivot element
Such that the elements less than pivot element should come before pivot element
Note: Preserve order while shifting
"""


"""
Solution:
Initialize two Linked Lists say, A & C
Let original Linked List be B
Iterate through B, if element is less than pivot element then insert it in A and delete from B
if element is greater than pivot element insert into C and delete from B
if element is equal to B do nothing.
Now merge in this order A-B-C
"""