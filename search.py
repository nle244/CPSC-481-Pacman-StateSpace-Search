# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # I just re wrote it again because for some reason in programming, it's always 
    # easier to write code than to read it, so it was easier to just reattempt it
    visited = []
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    while not stack.isEmpty():
        temp = stack.pop()
        if problem.isGoalState(temp[0]):
            return temp[1]
        if temp[0] in visited:
            # return control back to the beginning of the loop
            continue
        visited.append(temp[0])
        for node in problem.getSuccessors(temp[0]):
            if node[0] in visited:
                # return control
                continue
            stack.push((node[0], temp[1] + [node[1]]))
    util.raiseNotDefined()



# the previous code is down below




#     path = []
#     visited = list()
#     unvisited = util.Stack()
#     unvisitedList = list()

#     start = problem.getStartState()

#     ##unvisited.push(start)
#     if problem.isGoalState(start):  ##if the start is the goal, there is no path
#         return path
    
#     visited.append(start)
#     for node in problem.getSuccessors(start):
#         if node[0] not in visited:
#             unvisited.push(node)
            
#     while unvisited:
#         currentNode = unvisited.pop()
# ##        print("Current node: ",currentNode)
# ##        print("visited: ",visited)
#        ## if bool(visited): ## if visited is empty, no path to append
#         path.append(currentNode[1])

#         if problem.isGoalState(currentNode[0]):
# ##            print("Path found! Returning: ",path)
#             return path
#         else:
# ##            print("Goal not found... looking for children.")
#             visited.append(currentNode[0])
#             getChildren = False
#             for node in problem.getSuccessors(currentNode[0]):
# ##                print("node: ",node)
#                 if node[0] not in visited:
#                     getChildren = True
#                     unvisited.push(node)
# ##                    print("Children found... adding: ",node)
#             if not getChildren:
# ##                print("No children found... removing dead end.")
#                 path.pop()
            
#     return [] ##if the loop ends there is no valid path

    
##    visited.append(problem.getStartState())
##    unvisited.push(problem.getStartState())
##
##    while unvisited:
##        currentNode = unvisited.pop()
##        print("currentNode: ",currentNode)
##
##        visited.append(currentNode[0])
##        print("visited: ",visited)
##         ##if the currentNode is not the starting point 
##            path.append(currentNode[1])
##            print("path: ",path)
##
##        if problem.isGoalState(currentNode[0]): 
##            return path
##        else:
##            getChildren = list()
##            for node in problem.getSuccessors(currentNode[0]):
##                if node[0] not in visited:
##                    print("Adding: ",node)
##                    unvisited.push(node)
##            if not getChildren:
##                print("No children found, removing dead end.")
##                path.pop()
##            print("Goal not found... searching for children")
##            if problem.getSuccessors(currentNode[0]):  ##if there are children add them
##                print("Children found...")
##                for node in problem.getSuccessors(currentNode[0]):
##                    if node[0] not in visited:
##                        print("Adding: ",node)
##                        unvisited.push(node)
##            else:   ##if there are no successors path is a dead end
##                print("No children found, removing dead end.")
##                path.pop() 

##    return [] ##if we make it out of the loop there is no path
    
    
##    for each in visited:
##        for i in problem.getSuccessors(each):
##            unvisited.push(i)
##    visited.append(problem.getStartState())
##    print("Adding children of first node")
##    for node in problem.getSuccessors(visited[0]):
##        print("Child node: ",node)
##        if node not in visited:
##            ##print("Adding: ",node)
##            unvisited.push(node)
##            unvisitedList.append(node)
##
##    while unvisited:
##        currentNode = unvisited.pop()
##        visited.append(currentNode[0])
##        path.append(currentNode[1]) ##add to the path
####        print("Unvisited List: ",unvisitedList)
####        print("Visited: ",visited)
##        print("Exploring path: ", path)
##        print("Current node: ",currentNode)
##        
##        if problem.isGoalState(currentNode[0]):  ##if we found the goal return
##            print("Found the goal!")
##            return path
##        else:
##            print("did not find goal...")
##            print("Checking for successors: ",problem.getSuccessors(currentNode[0]))
##            if not (problem.getSuccessors(currentNode[0])): ##if there are no successors this is a dead end so remove from path
##                removed = path.pop()
##                print("no successors. removed: ",removed)
##            else:
##                print("Found successors... adding unvisited nodes.")
##                for node in problem.getSuccessors(currentNode[0]):
##                    print("i: ",node[0])
##                    print("visited: ",visited)
##                    print("unvisitedList: ",unvisitedList)
##                    print("i not in visited and i not in unvisitedList: ",node[0] not in visited and node not in unvisitedList)
##                    if node[0] not in visited and node not in unvisitedList:  ##only add if we haven't been there before
##                        unvisited.push(node)
##                        unvisitedList.append(node)
##                        print("Adding: ",node)
##        
##    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch