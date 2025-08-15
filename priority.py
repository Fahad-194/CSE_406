n= int(input ("Enter number of processes:"))
p=[]
for i in range (n):
    
    pid=f"P{i+1}"
    at=int(input(f"Ente5r arrival time for {pid}:"))
    bt=int(input(f"Enter burst time for {pid}:"))
    pt=int(input(f"Enter priority for {pid}:"))
    p.append([pid,at,bt,pt])

com=0
c_t=0
com_t=[0]*n
wt=[0]*n
ta=[0]*n
done=[False]*n

while com<n:
    index=-1
    highest_pri=100000
    for i in range(n):
        if p[i][1]<=c_t and not done[i]:
            if p[i][3]<highest_pri:
                highest_pri=p[i][3]
                index=i
    if index==-1:
        c_t=c_t+1
    else:
        wt[index]=max(0, c_t - p[index][1])
        c_t=c_t+p[index][2]
        ta[index]=wt[index]+p[index][2]
        com_t[index]=c_t
        done[index]=True
        com=com+1

print("\nPID\tAT\tBT\tPr\tCT\tTA\tWT")
total_ta=0
total_wt=0
for i in range(n):
    total_ta+=ta[i]
    total_wt+=wt[i]
    print (f"{p[i][0]}\t{p[i][1]}\t{p[i][2]}\t{p[i][3]}" 
          f"\t{com_t[i]}\t{ta[i]}\t{wt[i]}")
avg_ta=total_ta/n
avg_wt=total_wt/n
print(f"\nAverage Turnaround Time: {avg_ta}")
print(f"Average Waiting Time: {avg_wt}")
