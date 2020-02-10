def swap(t,i,j):
    save = t[i]
    t[i]=t[j]
    t[j]=save

def test_swap():
    t=[1,2,3,4,5,6]
    swap(t,1,3)
    return t==[1,4,3,2,5,6] and not t==[1,2,3,4,5,6]