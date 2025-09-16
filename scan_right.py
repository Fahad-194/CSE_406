requests = list(map(int, input("Enter requests :").split()))
head=int(input("Enter head position: "))

original_head = head
requests.sort()
seek_sequence = []
seek_count = 0

left=[r for r in requests if r < head]
right=[r for r in requests if r >= head]

for r in right:   
    seek_sequence.append(r)
    seek_count += abs(head - r)
    head = r
for r in reversed(left):     
    seek_sequence.append(r)
    seek_count += abs(head - r)
    head = r
print("Seek Sequence:", [original_head] + seek_sequence)
print("Total Head Movement:", seek_count)



