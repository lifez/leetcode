# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        location = [0, 0]
        
        movement = {'U': 1, 'D': -1, 'L': -1, 'R': 1}
        
        for move in moves:
            current_move = movement[move]
            if move in ['U', 'D']:
                location = [location[0], location[1] + current_move]
            else:
                location = [location[0]+ current_move, location[1]]
        
        return location == [0,0]
                

# Faster solution
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count('R') == moves.count('L'))  & (moves.count('U') == moves.count('D'))
