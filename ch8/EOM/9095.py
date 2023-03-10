# 1,2,3, 더하기 
# https://www.acmicpc.net/problem/9095
# 정수 N 이 주어 졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수 
 

# 바닥 타일이랑 비슷한 문제인듯
# d[1] = 1
# d[2] = 2
# d[3] = 4
# d[4] = 7
# d[5] = 13
# d[6] = 24
# d[i] = d[i-3] + d[i-2] + d[i-1]
# 1 추가 하는 방법 (1)-> 1개 -> d[i-1] * 1
# 2 추가하는 방법 (1+1,2) -> 2개 
# 2 (1+1) 은 1에서 이미 고려됨 -> d[i-2] * 1
# 3 추가하는 방법 (1+1+1+1 , 1+2,2+1, 3) 
# 3 (1+1+1 / 1+2 / 2 + 1) 도 1과 2에서 고려됨 -> d[i-3] * 1


T = int(input())
for _ in range(T):
    N = int(input())
    d = [0] * 4
    d[1],d[2],d[3] = 1,2,4
    
    for i in range(4,N+1):
        d_i = d[i-1] + d[i-2] + d[i-3] 
        d.append(d_i)

    print(d[N])






