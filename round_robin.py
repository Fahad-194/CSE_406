n=int(input("Enter number of processes:"))
p=[]
for i in range(n):
    at=int(input(f"Enter arrival time for P{i+1}:"))
    bt=int(input(f"Enter burst time for P{i+1}:"))
    p.append([i,f"P{i+1}",at,bt,bt])
t_q=int(input("Enter TimeQuant:"))
time=0
ready_queue=[]
complete=0
running_queue=[False]*n
ct=[0]*n
tat=[0]*n
wt=[0]*n
p.sort(key=lambda x:x[2])
ready_queue.append(0)
running_queue[0]=True
time=p[0][2]
while complete<n:
    if ready_queue:
        i=ready_queue.pop(0)
        if p[i][4]>t_q:
            time+=t_q
            p[i][4]-=t_q
        else:
            time+=p[i][4]
            p[i][4]=0
            idx=p[i][0]
            ct[idx]=time
            tat[idx]=ct[idx]-p[i][2]
            wt[idx]=tat[idx]-p[i][3]
            complete+=1
        for j in range(n):
            if not running_queue[j] and p[j][2]<=time:
                ready_queue.append(j)
                running_queue[j]=True
        if p[i][4]>0:
            ready_queue.append(i)
    else:
        for j in range(n):
            if not running_queue[j]:
                ready_queue.append(j)
                running_queue[j]=True
                time=p[j][2]
                break
p.sort(key=lambda x:x[0])
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
total_wt=0
for process in p:
    i=process[0]
    print(f"{process[1]}\t{process[2]}\t{process[3]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
    total_wt+=wt[i]
print(f"\nAverage Waiting Time: {total_wt/n}")
