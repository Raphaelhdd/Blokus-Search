import math

from board import Board
from search import SearchProblem, ucs
import util


class BlokusFillProblem(SearchProblem):
    """
    A one-player Blokus game as a search problem.
    This problem is implemented for you. You should NOT change it!
    """

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.expanded = 0

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        """
        state: Search state
        Returns True if and only if the state is a valid goal state
        """
        return not any(state.pieces[0])

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, 1) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)


#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################
class BlokusCornersProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.expanded = 0
        "*** YOUR CODE HERE ***"
        self.board = Board(board_w,board_h,1,piece_list,starting_point)
        self.current = starting_point
    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        "*** YOUR CODE HERE ***"
        return (state.state[0][0] != -1) and (state.state[0][state.board_w -1] != -1) and \
               (state.state[state.board_h -1][0] != -1) and (state.state[state.board_h -1][state.board_w -1] != -1)

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        "*** YOUR CODE HERE ***"
        return sum(action.piece.get_num_tiles() for action in actions)

def blokus_corners_heuristic(state, problem):
    """
    Your heuristic for the BlokusCornersProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come up
    with an admissible heuristic; almost all admissible heuristics will be consistent
    as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the other hand,
    inadmissible or inconsistent heuristics may find optimal solutions, so be careful.
    """
    "*** YOUR CODE HERE ***"
    corners = [(0, 0), (0, state.board_w - 1), (state.board_h - 1, 0), (state.board_h - 1, state.board_w - 1)]
    unreached_corners = [corner for corner in corners if state.state[corner[0]][corner[1]] == -1]
    if not unreached_corners:
        return 0
    perimeter = 2 * state.board_w + 2 * state.board_h
    min_moves = perimeter
    for corner in unreached_corners:
        min_distance = perimeter
        for row in range(state.board_h):
            for col in range(state.board_w):
                if state.state[row][col] != -1:
                    distance = infinity_norm_distance(corner,(row,col))
                    min_distance = min(min_distance, distance)
        min_moves = min(min_moves, min_distance)
    return min_moves

class BlokusCoverProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0), targets=[(0, 0)]):
        self.targets = targets.copy()
        self.expanded = 0
        "*** YOUR CODE HERE ***"
        self.board = Board(board_w,board_h,1,piece_list,starting_point)

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        "*** YOUR CODE HERE ***"
        for target in self.targets:
            x,y = target
            if state.state[x][y] == -1:
                return False
        return True

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        "*** YOUR CODE HERE ***"
        return sum(action.piece.get_num_tiles() for action in actions)

def infinity_norm_distance(point1, point2):
    row_diff = abs(point1[0] - point2[0])
    col_diff = abs(point1[1] - point2[1])
    distance = max(row_diff, col_diff)
    return distance

def blokus_cover_heuristic(state, problem):
    "*** YOUR CODE HERE ***"
    uncovered_targets = [(target[0], target[1]) for target in problem.targets if state.state[target[0]][target[1]] == -1]
    if not uncovered_targets:
        return 0
    max_distance_targets = 0
    if len(uncovered_targets) == 1:
        max_distance_targets = 1
    else:
        for i, target in enumerate(uncovered_targets):
            min_temp = float('inf')
            for target_bis in uncovered_targets[i + 1:]:
                min_temp = min(min_temp,infinity_norm_distance(target, target_bis))
            if min_temp != float('inf'):
                max_distance_targets += min_temp
    # print(f"DIstance : {max_distance_targets}\n,")
    unfilled_cases = sum(
        1 for row in range(state.board_h) for col in range(state.board_w) if state.state[row][col] == -1)
    surface = state.board_w * state.board_h
    # print(max_distance_targets * (len(uncovered_targets) / len(problem.targets)) * (unfilled_cases / surface))
    return max_distance_targets * (len(uncovered_targets) / len(problem.targets)) * (unfilled_cases / surface)


