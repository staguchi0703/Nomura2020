def resolve():
    '''
    code here
    '''
    H1, M1, H2, M2, K = [int(item) for item in input().split()]
 
    H = H2 -H1
    M = M2 -M1
    print(H*60 + M - K)
if __name__ == "__main__":
    resolve()
