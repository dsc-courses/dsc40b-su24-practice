---
tags: [graph theory, connected components]
---

Suppose an undirected graph $$G = (V,E)$$ has two connected components, $$C_1$$ and $$C_2$$. Suppose that $$|C_1| = 4$$ and $$|C_2| = 3$$. What is the largest that $$|E|$$ can possibly be?

[[Answer: 9. To load a graph with the most edges, make each connected component "fully connected". The most edges we can put in a component with 4 nodes is $$4 * 3 / 2 = 6$$, and the most we can put into a component with 3 nodes is $$3 * 2 / 2 = 3$$. Therefore, we can put at most 9 edges in this graph.]]
