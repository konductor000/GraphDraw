# GraphDraw

---

## Description

DrawGraph is a utility that allows you to draw a graph using its edges

### Technologies

- Python 3.8
- Plotly

---

## Installation

#### Clone the repository

```html
git clone https://github.com/konductor000/GraphDraw.git
```
#### You will also need to install Plotly

``` html
pip install plotly 
```

### How To Use

#### See tests.py

To use you will only need the number of nodes and graph's edges
```html
from DrawGraph import DrawGraph

n = 6
edges = [
    (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 4), (3, 5), (3, 6), (5, 6)
]
DrawGraph(n, edges)
```

### Examples

- Simple Graph
  ![Project Image](https://github.com/konductor000/GraphDraw/blob/master/images/pic2.PNG)

- Binary Tree
  ![Project Image](https://github.com/konductor000/GraphDraw/blob/master/images/pic1.PNG)


---

### How does it work


To arrange the nodes on the plane, I used the **annealing method**.
Initially, the nodes are placed randomly and subsequently
moved to a random position, with each iteration, intersections
are counted, the fewer intersections, the higher the chance
that the node will be moved

To display the result I used the **plotly** library

DrawGraph.py file creates a plane with nodes.

Draw.py file draws graph using plotly
