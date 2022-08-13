# Graph Coloration

### The project

This project consists on the separation in two or three (NP problem) classes (here it's represented by the coloration) of the nodes in a graph.

The nodes are object created as instance of the class point and the graph is an instance of the class graphe.

An instance of the class point has three attributes:  
-a name (string)  
-a color (null string at the beginning)  
-coordinates (tuple of ints)  

An instance of the class graphe has three attributes:  
-V is the list of all the nodes (list of instances of point)  
-E is the list of all the links between nodes (list of tuples containing two instances of point)  
-C is the list of colors available for coloration (list of string)

The class function couleur2 colors the graphe in two colors (if their is two different colors in C) and couleur3 colors it in three.

I also implemented pygame to show the results in a visual way.

### Conclusion

It's a good way to discover graph theory as it's not the most difficult project and we can easily imagine it's usage: an algorithm to fill a calendar and make sure someone is at one place and not more during the day.
