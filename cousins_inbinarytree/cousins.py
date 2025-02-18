import networkx as nx
import matplotlib.pyplot as plt


def plot_recursion_tree(x, n):
    G = nx.DiGraph()

    def helper(x, n, parent=None):
        # Add the node to the graph
        G.add_node((x, n), label=f'helper({x}, {n})')
        if parent is not None:
            G.add_edge(parent, (x, n))

        # Base case
        if n == 0:
            return 1

        half = helper(x, n // 2, (x, n))  # Recur for n // 2
        if n % 2 == 0:
            return half * half  # Even power
        else:
            return half * half * x  # Odd power

    helper(x, n)

    # Draw the recursion tree
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels, font_size=9)
    plt.title(f"Recursion Tree for helper({x}, {n})")
    plt.show()


# Example: plot recursion tree for helper(2, 5)
plot_recursion_tree(2, 5)
