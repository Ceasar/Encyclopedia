
================================================================================
Palantir
================================================================================

- Founded 2004; raised $301M;

.. contents::

Technology
================================================================================

Palantir's engineering team is organized into three sub-teams: UX, platform, and
infrastructure.

The degree of code quality varies across teams and part of the project. Older
code is not necessarily written well. Further, teams closer to the front-end
tend to work faster. Overall, much more emphasis is being placed on writing code
"the right way" these days.

Historically[*]_, Palantir team organization was loose, and engineers shuffle
around to work on different features. Recently, team organization was redesigned
such that for a given feature, a group of people kind of own that feature and
tend to work on features together. (By corollary, if someone want to change
something, they consult that team.)

Engineering teams do not have managers, but has team leads which fulfill a
similar role. Team leads are responsible for organizing teams in a sensible way,
assign resources (e.g. QE), and interfacing between various teams.

On the search team, there is about 10 people, 6 devs.

Decision making is made at various levels. Strategic decisions are made at a
high level. Implementation details are made at a low-level, as a team. Inbetween
features are assigned every couple of month, partially matching interests.

Screening
================================================================================

Take home
--------------------------------------------------------------------------------

.. raw:: html

    <script src="https://gist.github.com/Ceasar/8405443.js"></script>

Phone screen
--------------------------------------------------------------------------------

Essentially, implement BFS and DFS. [*]_

.. code::

    class Tree:
        def get_data():
            pass
        
        def get_children():
            pass


    def dfs(tree, data):
        if tree.get_data() == data:
            return 0
        else:
            children = tree.get_children()
            for child in children:
                try:
                    return 1 + dfs(child, data)
                except ValueError:
                    pass
            raise ValueError("data not in tree")


    def _bfs(nodes, data):
        if not nodes:
            raise ValueError("data not in tree")
        new_nodes = []
        for node in nodes:
            if node.get_data() == data:
                return 0
            new_nodes.extend(node.get_children())
        return 1 + _bfs(new_nodes, data)
        
    def bfs(tree, data):
        return _bfs([tree], data)

    """
    def bfs(tree, data):
        depth = 0
        nodes = [tree]
        while len(nodes) > 0:
            for node in nodes:
                if node.get_data() == data:
                    return depth
            depth += 1
            nodes = sum(node.get_children() for node in nodes, [])
        raise ValueError("data not in tree")
    """


.. [*]
    Based on an interview with a new grad on search (infrastructure) team on
    January 15, 2014.
