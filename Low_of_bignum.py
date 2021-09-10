def sol():
    #변수할당
    n, m ,k = map(int, input().split())
    #n=배열길이 m=만큼 더해야함 k= 제한횟수
    data = list(map(int, input().split()))
    data.sort()
    data
    first = data[-1]
    second = data[-2]
    answer=0
    count=0
    while count < m :
        for i in range(0,k):
            count+=1
            answer+=first
        answer+=second
        count+=1
    print(answer)

