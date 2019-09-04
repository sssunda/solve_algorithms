def solution(N, stages):
    answer = []
    fail = []

    zero = set([x+1 for x in range(N)])
    stage = set(stages)

    zero = list(zero - stage)

    stage = list(stage)
    stage.sort()
    if stage.count(N+1) > 0 :
        stage.remove(N+1)

    member = len(stages)
    for s in (stage):
        cnt = stages.count(s)
        fail.append((-cnt/member, s))
        member -= cnt

    fail.sort()
    answer = list(map(lambda x : x[1], fail))
    zero.sort()
    answer += zero

    return answer

if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
    