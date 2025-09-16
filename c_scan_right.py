requests=list(map(int,input("Enter sequence:").split()))
h=int(input("Enter head position"))
original_h=h

requests.sort()
seek_sequence=[]
seek_count=0

left=[r for r in requests if r<h]
right=[r for r in requests if r>h]

if h in requests:
    seek_sequence.append(h)
for r in right:
    seek_sequence.append(r)
    seek_count+=abs(h-r)
    h=r
if left:
    smallest=min(requests)
    seek_count+=abs(smallest-h)
    h=smallest
    for r in left:
        seek_sequence.append(r)
        seek_count+=abs(h-r)
        h=r

print("Seek Sequence:",seek_sequence)
print("Total Head Movement:",seek_count)
