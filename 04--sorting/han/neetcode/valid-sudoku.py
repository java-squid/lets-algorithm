class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Each row must contain the digits 1-9 without repetition.        
        for i in range(len(board)):
            temp = [0] * 10
            for j in range(len(board[i])):
                cell = board[i][j]

                if cell == ".":
                    continue

                temp[int(cell)] += 1

                if temp[int(cell)] > 1:
                    return False

        # Each column must contain the digits 1-9 without repetition.
        for i in range(len(board)):
            temp = [0] * 10
            for j in range(len(board[i])):
                cell = board[j][i]

                if cell == ".":
                    continue

                temp[int(cell)] += 1

                if temp[int(cell)] > 1:
                    return False

        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        for i in range(3):
            for j in range(3):
                temp = [0] * 10
                for k in range(3):
                    for s in range(3):
                        cell = board[i * 3 + k][j * 3 + s]
                        if cell == ".":
                            continue

                        temp[int(cell)] += 1
                        if temp[int(cell)] > 1:
                            return False
        return True


# 참고
# 3x3 배열을 어떻게 탐색해야할지 감이 안왔음.. --> https://juni-dev-log.tistory.com/139
# set을 이용해서 풀수도 있을듯.