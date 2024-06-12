---
tags: [aggregate analysis]
---


Suppose the code below is run on a graph $$G = (V, E)$$. What is its time complexity? You may assume that $$|E| \geq 1$$.

```
for u in graph.nodes:
    for v in graph.neighbors(u):
        print(u, v)
```

( ) $$\Theta(E)$$
( ) $$\Theta(V)$$
(x) $$\Theta(V + E)$$
( ) $$\Theta(V^2)$$
( ) $$\Theta(VE)$$

[[$$\Theta(V + E)$$]]
