"""
In search.py, you will implement generic search algorithms
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # problem cest BlokusFillProblem
    # print("Start: \n", problem.get_start_state()) # cest le board
    # print("Is the start a goal?", problem.is_goal_state(problem.get_start_state())) # est ce que le debut cest larrivee
    # print("Start's successors:", problem.get_successors(problem.get_start_state())) # avoir prochain state
    stack = util.Stack()
    stack.push((problem.get_start_state(), [], 0))
    visited_set = set()
    while not stack.isEmpty():
        current, path, cost = stack.pop()
        if problem.is_goal_state(current):
            return path
        if current not in visited_set:
            visited_set.add(current) # 10
            for successor, action, stepCost in problem.get_successors(current):
                if successor not in visited_set:
                    stack.push((successor, path + [action], stepCost))
    return []

def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    queue.push((problem.get_start_state(), [], 0))
    visited_set = set()
    while not queue.isEmpty():
        current, path, cost = queue.pop()
        if problem.is_goal_state(current):
            return path
        if current not in visited_set:
            visited_set.add(current)
            for successor, action, stepCost in problem.get_successors(current):
                if successor not in visited_set:
                    queue.push((successor, path + [action], stepCost))
    return []

def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    priority_queue.push((problem.get_start_state(), []), 0)
    cost_dict = {}
    cost_dict[problem.get_start_state()] = 0
    index_successor = 0
    visited_set = set()
    while not priority_queue.isEmpty():
        current, path = priority_queue.pop()
        if problem.is_goal_state(current):
            return path
        if current not in visited_set:
            visited_set.add(current)
            for successor, action, stepCost in problem.get_successors(current):
                new_cost = cost_dict[current] + stepCost
                if successor not in cost_dict or new_cost < cost_dict[successor]:
                    cost_dict[successor] = new_cost
                    priority = new_cost
                    priority_queue.push((successor, path + [action]), (priority,index_successor))
                    index_successor += 1
    return []


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    priority_queue.push((problem.get_start_state(), []), 0)
    cost_dict = {}
    cost_dict[problem.get_start_state()] = 0
    index_successor = 0
    visited_set = set()
    while not priority_queue.isEmpty():
        current, path = priority_queue.pop()
        if problem.is_goal_state(current):
            return path
        if current not in visited_set:
            visited_set.add(current)
            for successor, action, stepCost in problem.get_successors(current):
                new_cost = cost_dict[current] + stepCost
                if successor not in cost_dict or new_cost < cost_dict[successor]:
                    cost_dict[successor] = new_cost
                    priority = new_cost + heuristic(current,problem)
                    priority_queue.push((successor, path + [action]), (priority, index_successor))
                    index_successor += 1
    return []



# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
