import plotly.graph_objects as go


class Draw:
    def __init__(self, nodes_, edges_):
        self.nodes = nodes_
        self.n = len(self.nodes) - 1
        self.edges = edges_
        self.g = [[] for i in range(self.n + 1)]

        for x, y in self.edges:
            self.g[x].append(y)
            self.g[y].append(x)

    def draw(self):
        edge_x = []
        edge_y = []

        for edge in self.edges:
            x0, y0 = self.nodes[edge[0]].x, self.nodes[edge[0]].y
            x1, y1 = self.nodes[edge[1]].x, self.nodes[edge[1]].y
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        node_x = []
        node_y = []

        for i in range(1, len(self.nodes)):
            x, y = self.nodes[i].x, self.nodes[i].y
            node_x.append(x)
            node_y.append(y)

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                color=[],
                size=10
            ),
            line_width=2)

        node_adjacencies = []
        node_text = []
        for i in range(1, self.n + 1):
            node_adjacencies.append(len(self.g[i]))
            node_text.append('Connections: ' + str(len(self.g[i])) + ', node: ' + str(i))

        node_trace.marker.size = node_adjacencies
        node_trace.text = node_text

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Тестовый граф для NTA',
                            titlefont_size=16,
                            showlegend=False,
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        fig.show()


if __name__ == '__main__':
    d = Draw
