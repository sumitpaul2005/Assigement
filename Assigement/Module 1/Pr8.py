def find(m,s):
    con = []
    for i in m:
        if i in s:
            con.append(i)
    if len(con) == 0:
        print("Not found sub string")
    else:
         print("Found in Sub list : ",con)
    
    
main = list(map(int, input("Enter the main list : ").split()))
sub = list(map(int, input("Enter the sub list : ").split()))
find(main,sub)