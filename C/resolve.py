def resolve():
    '''
    code here
    '''
    N = int(input())
    A_list = [int(item) for item in input().split()]
    
    hp = sum(A_list) #leaf
    is_slove = True
    res = 1 # root
    prev = 1
    prev_add_num = 0
    delete_cnt = 0
    if hp > 2**N:
        is_slove = False
    elif A_list[0] == 1:
        if len(A_list) >= 2:
            if sum(A_list[1:]) >= 1:
                is_slove = False
    else:
        for i in range(1, N+1):
            if 2**i >= A_list[i]:
                add_num = min(2**(i-1) - prev_add_num, hp)
                res += add_num
                hp -= A_list[i]
                prev = A_list[i]
                prev_add_num = add_num
            else:
                is_slove = False
                break
            print(i, prev, hp, res)

    print(res) if is_slove else print(-1)


if __name__ == "__main__":
    resolve()
