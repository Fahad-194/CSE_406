requests=list(map(int,input("Enter disk reuquests:").split()))
head=int(input("Enter head:"))
current=head
total_seek_t=0
print("Sequence:",current,end="")
if head in requests:
    requests.remove(head)
while requests:
    closest=requests[0]
    min_distance=abs(current-closest)
    for i in requests:
        distance=abs(current-i)
        if distance<min_distance:
            min_distance=distance
            closest=i
    print("-->",closest,end="")
    total_seek_t+=min_distance
    current=closest
    requests.remove(closest)
print("\nTotal Seek Time:",total_seek_t)