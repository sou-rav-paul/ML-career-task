strng='banana'
freq={}
for alphabet in strng:
    if not  alphabet in freq:
        freq[alphabet]=1
    else:
        freq[alphabet]+=1
for k,v in freq.items():
    print('For :',k,'Count :',v)