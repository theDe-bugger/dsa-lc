###
# You're a hero hunting for treasure in a dungeon. Unfortunately, the dungeon is riddled with traps of varying deadliness 
# and there may not even be a treasure. The basic goal is to find the treasure in the least amount of steps, with 
# the most amount of health. Without dying.
# • Dungeon represented by an NxM array of characters
# • Starting location of 0,0
# • Starting health of 5
# • Death occurs when you are at 0 health
# "is an empty space that can be walked through.
# 0,0 is always empty.
# • 'X' is an impassable wall.
# • A digit [0-9] is a trap, where the value is the amount of damage it does. There may be many.
# • 'T' is the treasure. There are 0 or 1 in a maze.
# • Orthogonal traversal only (up, down, left, right)


# Given a dungeon, return a pair of integers representing the minimum number of steps to reach the treasure, and the maximum amount
# of health after reaching the treasure (or the same path). Always prioritize minimum number of steps, and then maximum amount of health.
# • If there is no solution, return (-1, 5) .
# • If there is a tie breaker, return the maximum health of all shortest paths. For example, 
# if two paths can reach the treasure in 5 steps, but one leaves the player with 2 health and the other 4 health, 
# the solution would be (5, 4).


# Example:
# dungeon = [
# ['', 'X' ],
# ['2', 'T']
# # Min number of steps, max amount of
# health after reaching the treasure
# Solution: 2, 3
###


from collections import deque
def get_valid_neighbours(dungeon,currNode):
    positions = []
    xmax = len(dungeon)
    ymax = len(dungeon[0])
    currPos, currSteps, currHealth = currNode
    currx,curry = currPos
    for x in range(-1,2,1):
        for y in range(-1,2,1):
            # print((x,y))
            if 0 <= currx + x and currx+x < xmax:
                if 0<= curry + y and curry+y < ymax:
                    if (y != x) and dungeon[currx+x][curry+y] != "X":
                        print(f"Found valid pos: {currx+x, curry+y} at {dungeon[currx+x][curry+y]}")
                        positions.append([(currx + x, curry + y),currSteps + 1,currHealth - (0 if dungeon[currx+x][curry+y] == ' ' or dungeon[currx+x][curry+y] == 'T' else int(dungeon[currx+x][curry+y]))])
    print(positions)
    return positions

def dungeon_bfs(dungeon):
    startPos = (0,0)
    visited = [[False] * len(dungeon[0]) for i in range(len(dungeon))]
    print(visited)
    visited[startPos[0]][startPos[1]] = True
    q = deque()
    
    minsteps = len(dungeon[0]) * len(dungeon) * 2
    maxhealth = 0
    q.append([startPos,0,5])
    while q:
        currNode = q.popleft()
        currPos, currSteps, currHealth = currNode
        print(currPos)
        if dungeon[currPos[0]][currPos[1]] == "T":
            if currSteps < minsteps:
                minsteps = currSteps
                maxhealth = currHealth
            elif currSteps == minsteps:
                maxhealth = max(maxhealth,currHealth)
            continue
            
        for neighbor in get_valid_neighbours(dungeon,currNode):
            neighborPos, neighborSteps, neighborHealth = neighbor
            print(neighborPos)
            print(visited)
            if not visited[neighborPos[0]][neighborPos[1]]:
                visited[neighborPos[0]][neighborPos[1]] = True
                print("appending to q")
                q.append(neighbor)
    return (minsteps,maxhealth) if maxhealth != 0 else (-1,5)

def test_find_treasure():
    dungeon1 = [
        [' ', 'X'],
        ['2', 'T']
    ]
    assert dungeon_bfs(dungeon1) == (2, 3)

    dungeon2 = [
        [' ', ' ', ' '],
        [' ', 'X', ' '],
        [' ', '3', ' ']
    ]
    assert dungeon_bfs(dungeon2) == (-1, 5)

    dungeon3 = [
        [' ', '1', 'T'],
        [' ', 'X', ' '],
        [' ', '2', ' ']
    ]
    assert dungeon_bfs(dungeon3) == (2, 4)

    dungeon4 = [
        [' ', '1', ' '],
        ['2', 'X', ' '],
        [' ', '2', 'T']
    ]
    assert dungeon_bfs(dungeon4) == (4, 4)

    dungeon5 = [
        [' ', 'X', ' '],
        ['X', 'X', ' '],
        [' ', ' ', 'T']
    ]
    assert dungeon_bfs(dungeon5) == (-1,5)

    dungeon6 = [
        [' ', 'X', ' '],
        ['X', 'X', ' '],
        [' ', 'X', 'T']
    ]
    assert dungeon_bfs(dungeon6) == (-1, 5)
    
    # dungeon7 = [[' ', ' ', ' ', ' ', ' '], 
    #             [' ', 'X', 'X', 'X', ' '], 
    #             [' ', 'X', ' ', ' ', ' '], 
    #             [' ', 'X', '3', 'X', 'X'], 
    #             [' ', '4', ' ', '1', 'T']]
    # assert dungeon_bfs(dungeon7) != (-1, 5)
    
    dungeon8 = [[' ', ' ', 'H'], [' ', 'X', 'X'], [' ', '9', 'T']]
    print(dungeon_bfs(dungeon8))
    print("All test cases pass")

test_find_treasure()