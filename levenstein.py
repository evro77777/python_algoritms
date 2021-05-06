# def levenstein(a,b):
#     f = [[(i+j) if i*j == 0 else 0 for j in range(len(b)+1)] for i in range(len(a)+1)]
#     print(f)
#
# levenstein("abc","bcd")
def search_substr(s,sub):
    for i in range(0,len(s)-len(sub)+1):
        
            print(i)
search_substr("abcdabfab","ab")