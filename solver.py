n=10
def check_pos(x,y):
    def diagonal_handler(l):
        return list(filter(lambda tup: not ((tup[0] <= 0) or (tup[0] > n)) and not ((tup[1] <= 0) or (tup[1] > n)),l))
    return set([(x,j) for j in range(1,n+1)]+[(i,y) for i in range(1,n+1)]+diagonal_handler([(x+i,y+i) for i in range(-2*n,2*n)])\
           +diagonal_handler([(x+i,y-i) for i in range(-2*n,2*n)])\
           +diagonal_handler([(x-i,y+i) for i in range(-2*n,2*n)])+diagonal_handler([(x-i,y-i) for i in range(-2*n,2*n)]))
total_set={(x,y):check_pos(x,y)for x in range(1,n+1)for y in range(1,n+1)}
def connector(list_):
    check_places=set()
    [check_places.update(list(total_set[x])) for x in list_]
    return check_places
def solver(q_list,iter_):
    if iter_ == n :
        check_places=connector(q_list)
        q_rem = (n,{x for x in range(1, n + 1)}.difference({x[1] for x in q_list}).pop())
        if not(q_rem in check_places):
            q_list.append(q_rem)
            print(q_list)
    else:
        for i in range(1,n+1):
            check_position=connector(q_list)
            if (iter_,i) in check_position :
                q_list_lier=[x for x in q_list if x[0]==iter_]
                if q_list_lier:
                    q_list.remove(q_list_lier.pop())
                continue
            q_list.append((iter_,i))
            solver(q_list,iter_+1)
            q_list.pop()
[solver(q_list=[(1,y)],iter_=2) for y in range(1,n+1) ]