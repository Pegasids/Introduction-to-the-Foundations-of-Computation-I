def swap(lst,k,l):
    original_k = lst[k]
    lst[k] = lst[l]
    lst[l] = original_k
    
def numerize(lst):
    lst = [int(i) for i in lst]
    return lst

def bubble(lst):
    for i in range (len(lst)):
        for elem in range(len(lst) - 1):
            if lst[elem] >= lst[elem + 1]:
                k = elem
                l = elem + 1
                swap(lst,k,l)
    return lst

def merge(lst1, lst2):
    i = 0
    j = 0
    dct = []
    try:
        while i <= len(lst1) - 1 or j <= len(lst2) - 1:
            
            if lst1[i] < lst2[j]:
                dct.append(lst1[i])
                i += 1
                if lst2[j] < lst1[i]:
                    dct.append(lst2[j])
                    j += 1
                else:
                    dct.append(lst1[i])
                    i += 1
                    
            elif lst2[j] < lst1[i]:      
                dct.append(lst2[j])
                j += 1
                if lst2[j] < lst1[i]:           
                    dct.append(lst2[j])
                    j += 1
                else:       
                    dct.append(lst1[i])
                    i += 1
                    
            elif lst2[j] == lst1[i]:       
                dct.append(lst2[j])
                dct.append(lst1[i])
                j += 1
                i += 1
                
    except:
        IndexError
    
    for n in range (j, len(lst2)):
            dct.append(lst2[n])
    for n in range (i, len(lst1)):
            dct.append(lst1[n])
    
    return dct 

def show(lst):
    out = ""
    for elem in lst:
        out = out + str(elem) + ' '
    return out

lst1 = str(input("Enter list1: "))
lst2 = str(input("Enter list2: "))
print("list1:",lst1)
print("list2:",lst2)
print("list1 sorted:",show(bubble(numerize(lst1.split()))).strip())
print("list2 sorted:",show(bubble(numerize(lst2.split()))).strip())
print("The merged list is:", show(merge(bubble(numerize(lst1.split())), bubble(numerize(lst2.split())))).strip())