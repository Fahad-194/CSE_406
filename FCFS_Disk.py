requests=list(map(int,input("Enter disk requests:").split()))
head=int(input("Enter head postion: "))
total_distance = 0
current = head
print("Seek sequence:",current,end=" ")
for i in requests:
    if i==head:
        continue
    else:
        print("->",i, end=" ")           
        total_distance+=abs(current-i)      
        current=i                        
print("\nTotal Seek Time:", total_distance)