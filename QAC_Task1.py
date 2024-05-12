import random

def generate_random_list(n : int):
    random_list=[]
    max_number=2**n
    #generate random number k
    k = random.randrange(1,max_number+1)
    # generate a list with of 2n unique random positive number
    while (len(random_list)<2*n):
        new_number = random.randint(1,max_number+1)
        #print(new_number)
        if new_number not in random_list:
            random_list.append(new_number)
    return k, random_list

def search_k(k: int, list_n: list[int]):
    # sort list_n 
    list_n.sort()
    # binary search for the k in the list_n
    low = 0
    high = len(list_n) - 1
    #init step
    step =0
    while low <= high:
        step = step +1 # increase step 
        mid = (low + high) // 2
        if list_n[mid] == k:
            return (True, step)
        elif list_n[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return (False, step)

def less_than_k(k: int, list_n: list[int]):
    list_n.sort()
    list_nk=[]
    step=0
    for i in list_n:
        step = step+1
        if (i<k):
            list_nk.append(i)
        else:
            return ((list_nk), step)
    return ((list_nk), step)

k, list_n = generate_random_list(5)
list_nk = less_than_k(k, list_n)
print(k, list_n)
k_exist = search_k(k, list_n)
print(k_exist)
print(list_nk)
