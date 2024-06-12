---
tags: [hashing]
---


Suppose a hash table is constructed using linked lists to store the data within each bin, and that collisions are resolved by chaining. What is the *worst case* time complexity of inserting a new element into the hash table? You may assume that the hash table will not need to be resized, and that evaluating the hash function takes $$\Theta(1)$$ time.

(x) $$\Theta(1)$$
( ) $$\Theta(\log n)$$
( ) $$\Theta(n)$$
( ) $$\Theta(n \log n)$$
( ) $$\Theta(n^2)$$

[[$$\Theta(1)$$. Inserting an item into a hash table takes two steps: first, we hash the item to find its bin -- this takes $$\Theta(1)$$ time. Next, we actually insert the item into that bin. When we use chaining, we do this by appending the item to the linked list containing that bins elements. Appending to a linked list takes $$\Theta(1)$$ time, and so overall this takes $$\Theta(1)$$.]]
