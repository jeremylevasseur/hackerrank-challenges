if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = ()
    
    for i in range(n):
        t = t + (integer_list[i],)
    
    print(hash(t))
