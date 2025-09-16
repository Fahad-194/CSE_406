requests=list(map(int,input("Enter requests:").split()))
h=int(input("Enter head position:"))
original_h=h

requests.sort()
seek_sequence=[]
seek_count=0

left=[r for r in requests if r<h]
right=[r for r in requests if r>h]
if h in requests:
    seek_sequence.append(h)

for r in reversed(left):
    seek_sequence.append(r)
    seek_count+=abs(h-r)
    h=r

if right:
    largest=max(requests)
    seek_count+=abs(largest-h)
    h=largest
    for r in reversed(right):
        seek_sequence.append(r)
        seek_count+=abs(h-r)
        h=r

print("Seek Sequence:",seek_sequence)
print("Total Head Movement:",seek_count)
