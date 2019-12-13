def calc(cstate, past):
    nrow = len(cstate) + 1
    ncol = len(cstate[0]) + 1
    past = [[0] * ncol for _ in range(nrow)]
    chk = [0 for _ in range(nrow + 1)]
    memo = {}

    def subcalc(current, k):
        i, j = current
        if j == ncol:
            return 1
        preimages = 0
        index = ((i, j), tuple(chk))
        if index in memo:
            return memo[index]
        for cell in [0, 1]:
            if (i == 0 or j == 0) or ((past[i - 1][j - 1] + past[i - 1][j]
                                       + past[i][j - 1] + cell == 1) == cstate[i - 1][j - 1]):
                temp = chk[k]
                chk[k] = cell
                past[i][j] = cell
                preimages += subcalc(((i + 1) % nrow, j + (i + 1 == nrow)), (k + 1) % (nrow + 1))
                chk[k] = temp
        memo[index] = preimages
        return preimages

    answer = subcalc((0, 0), 0)
    return answer


def solution(g):
    prev = [[True] * (len(g[0]) + 1) for i in range(len(g) + 1)]
    return calc(g, prev)
