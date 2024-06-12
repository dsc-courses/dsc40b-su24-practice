---
tags: [depth first search]
---


Suppose a *depth* first search (DFS) is run on the graph shown below using node $$u_4$$ as the source and the convention that `graph.neighbors` produces nodes in ascending order by label. What will be the predecessor of $$u_6$$ in the DFS?

![](f1.png)

( ) $$u_1$$
( ) $$u_2$$
( ) $$u_3$$
( ) $$u_4$$
(x) $$u_5$$
( ) $$u_6$$
( ) $$u_7$$
( ) $$u_8$$
( ) $$u_9$$

[[$$u_5$$. DFS starts at $$u_4$$, looks at the neighbors, and sees $$u_2$$ is undiscovered, so it makes a recursive call `dfs(u_2)`. At $$u_2$$, it sees that $$u_1$$ is undiscovered, and calls `dfs(u_1)`. At $$u_1$$, there's nothing to do, so it's marked as visited and the recursion unrolls back to the call on `dfs(u_2)`. We then look at the next neighbor of $$u_2$$, which is $$u_3$$. We make a call to `dfs(u_3)`, which looks at its neighbors and sees $$u_5$$. We make a call to `dfs(u_5)`, and during this call we discover $$u_6$$, meaning that $$u_5$$ is the DFS predecessor of $$u_6$$.]]
