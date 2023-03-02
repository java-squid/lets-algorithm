import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    meetings_time_table = []

    for _ in range(N):
        start, end = map(int, input().split())
        meetings_time_table.append([start, end])

    # sorted by end time and sorted by start time
    meetings_time_table = sorted(meetings_time_table, key=lambda x: (x[1], x[0]))

    # print(meetings_time_table)

    count = 0
    current_end_time = 0 # 4
    for start, end in meetings_time_table:
        if start >= current_end_time:
            count += 1
            current_end_time = end

    print(count)


if __name__ == '__main__':
    solve()

# 문제 이해
# 한개의 회의실이 있고, 이를 이용할 수 있는 회의의 최대 갯수를 찾아야함.
# 이용할 수 있는 회의의 갯수를 최대로 하기 위해서는, 종료시간이 빨라야함 -> 종료시간 으로 오름차순 정렬해야함
# 문제 이해가 덜 되었음, 정렬을 끝나는 시간으로 한번, 시작하는 시간으로 해야되는걸 파악하는게 핵심인듯


# sudo code
# start, end = input()
# pq.put((start,end)) , tuple로 저장
# 모르겠음 -> 블로그 참고

# 제한
# 시작, 끝나는 시간에 0이 나올 수 있음.

# 참고
# https://jmcunst.tistory.com/49
