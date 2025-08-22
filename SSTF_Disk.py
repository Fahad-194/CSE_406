requests=list(map(int,input("Enter disk reuquests:").split()))
head=int(input("Enter head:"))
current=head
total_distance=0
print("Sequence:",current,end="")
if head in requests:
    requests.remove(head)
while requests:
    if requests[0]==head:
        closest=requests[1]
    else:
        closest=requests[0]
    min_distance=abs(current-closest)
    for i in requests:
        distance=abs(current-i)
        if distance<min_distance:
            min_distance=distance
            closest=i
    print("-->",closest,end="")
    total_distance+=min_distance
    current=closest
    requests.remove(closest)
print("\nTotal Distance:",total_distance)