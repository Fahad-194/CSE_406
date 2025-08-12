n= int(input ("Enter number of processes:"))
p=[]
for i in range (n):
    pid=input(f"Enter your process id P{i+1}:")
    bt=int(input(f"Enter burst time for{pid}:"))
    at=int(input(f"Ente5r arrival time for {pid}:"))
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

print("\nPID\tArrival_T\tBurst_T\tPriority\tCompletion\tTurn_A_T\tWaiting_T")
for i in range(n):
    print (f"{p[i][0]}\t{p[i][1]}\t{p[i][2]}\t{p[i][3]}" 
          f"\t\t{com_t[i]}\t{ta[i]}\t{wt[i]}")