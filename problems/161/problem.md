---
tags: [start and finish times, depth first search]
---


Suppose $$T = (V, E)$$ is a connected, undirected graph with no cycles (that is, $$T$$ is a tree). Suppose a depth first search is run on $$T$$ using node s as the source. Assume that node s has two neighbors: $$u$$ and $$v$$. If $$|V| = 15$$, which one of the below represents possible start and finish times of $$u$$ and $$v$$? You may assume that `graph.neighbors` produces neighbors in ascending order of label.

( ) `start[u] = 2`, `finish[u] = 10`, `start[v] = 8`, `finish[v] = 29`
(x) `start[u] = 2`, `finish[u] = 21`, `start[v] = 22`, `finish[v] = 29`
( ) `start[u] = 1`, `finish[u] = 16`, `start[v] = 17`, `finish[v] = 30`
( ) `start[u] = 16`, `finish[u] = 29`, `start[v] = 2`, `finish[v] = 15`


[[`start[u] = 2`, `finish[u] = 21`, `start[v] = 22`, `finish[v] = 29`]]
