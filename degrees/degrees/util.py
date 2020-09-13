class Node():
    def __init__(self, person, parent, movie):
        self.person = person
        self.parent = parent
        self.movie = movie

    def get_path(self):
        """
        Returns a list, where each list item is the next (movie_id, person_id) pair of the path to this node
        """
        path = []
        current = self
        while current.parent is not None:
            path.append((current.movie, current.person))
            current = current.parent
        path.reverse()
        return path


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_person(self, person):
        return any(node.person == person for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node