
import random
import csv


def random_subset(n, k) :
    VList = [value  for value in range(1,n)]
    changed_elements = {}
    for i in range (k) :
        # Generate a random index between j and n - 7, inclusive.
        rand_idx = random.randrange(1, n)
        rand_idx_mapped = changed_elements.get(rand_idx , rand_idx)
        #i_mapped = changed_elements.get(i , i)
        #changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped    
        # print(rand_idx)   
    return [changed_elements[i] for i in range(k)]    


def merge_two_sorted_lists(L1, L2):
    #place holder
    dummy_head = tail = ListNode()
    
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
        
    tail.next = L1 or L2
    return dummy_head.next
    
def make_lottery_dict(L):
    count = {}
    
    for i in L:
        count.setdefault(i, 0)
        count[i] = count[i] + 1
    return count

filename = 'output.csv'
outputfile = open(filename, 'w', newline='')
outputWriter = csv.writer(outputfile)

for j in range(100):
    output = random_subset(50,5)
    print_two = random_subset(12,2)
    outputWriter.writerow(output)
    #print(output)
    #print(print_two)
    #finalOutput = merge_two_sorted_lists(output,print_two)
    finalOutput = make_lottery_dict(output)
    #print(finalOutput)









