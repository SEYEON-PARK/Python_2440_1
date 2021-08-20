'''
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''

N=int(input()) # 사용자로부터 정수 입력받기
n=N # n에 N 값 저장하기

for i in range(n):
    for j in range(N, 0, -1):
        print("*", end="")
    print()
    N-=1
