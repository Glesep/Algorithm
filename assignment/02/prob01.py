import time

with open("./files/harry_full.txt", 'r', encoding='utf-8-sig') as f:
    lines = f.read().splitlines()
    words = [words for line in lines for words in line.split()]
    

def bubble_sort(words_copy):
    
    for i in range(len(words)-1, 0, -1):
        for j in range(0, i):
            if (words_copy[j] > words_copy[j+1]):
                words_copy[j], words_copy[j+1] = words_copy[j+1], words_copy[j]
                
    return words_copy

def insertion_sort(words_copy):

    for i in range(1, len(words_copy)-1):
        tmp = words_copy[i]
        j = i - 1
        
        while j > 0 and tmp < words_copy[j]:
            words_copy[j+1] = words_copy[j]
            j -= 1
            
        words_copy[j] = tmp   
    
    return words_copy

def merge(words_copy, start, mid, end):
    i = start
    j = mid+1
    tmp = []
    while (i <= mid and j <= end):
        if words_copy[i] <= words_copy[j]:
            tmp.append(words_copy[i])
            i+=1
        else:
            tmp.append(words_copy[j])
            j+=1
            
    while(i<=mid):
        tmp.append(words_copy[i])
        i+=1
    while(j <= end):
        tmp.append(words_copy[j])
        j+=1
    
    words_copy[start:end+1] = tmp
    return words_copy

def merge_sort(words_copy, start, end):
    mid = (start + end) // 2
    
    if start < end:
        words_copy = merge_sort(words_copy, start, mid)
        words_copy = merge_sort(words_copy, mid+1, end)
    
    return merge(words_copy, start, mid, end)

words_copied = words[0:len(words)//10]
start_time = time.time()
# bubble_sort(words_copy)
# words_copied = insertion_sort(words_copied)
words_copied = merge_sort(words_copied, 0, len(words_copied)-1)
end_time = time.time()
print(words_copied)
print (end_time - start_time)
            