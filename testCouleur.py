from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes with different background colors
dot.node('A', 'Node A', style='filled', fillcolor='lightblue')
dot.node('B', 'Node B', style='filled', fillcolor='lightgreen')
dot.node('C', 'Node C', style='filled', fillcolor='lightyellow')
dot.node('D', 'Node D', style='filled', fillcolor='lightpink')

# Add edges between nodes
dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('B', 'D')
dot.edge('C', 'D')

# Render the graph to a file
dot.render('couleurTest', format='png', cleanup=True)
