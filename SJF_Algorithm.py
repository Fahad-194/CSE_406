n=int(input("Enter Number of processes:"))
pros=[]
for i in range(n):
    pid = f"P{i+1}"
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))
    pros.append([pid, at, bt])
pros.sort(key=lambda x:x[1])
completed=[]
current_t=0
while pros:
    ready_pros=[]
    for i in pros:
        if current_t>=i[1]:
            ready_pros.append(i)
    if not ready_pros:
        current_t+=1
        continue
    ready_pros.sort(key=lambda x:x[2])
    current_pros=ready_pros[0]
    pros.remove(current_pros)
    pid=current_pros[0]
    at=current_pros[1]
    bt=current_pros[2]
    ct=current_t+bt
    tat=ct-at
    wt=tat-bt
    completed.append([pid,at,bt,ct,tat,wt])
    current_t=ct
completed.sort(key=lambda x:x[0])
print(f"\n{'Process':<8}{'AT':<10}{'BT':<10}{'CT':<10}{'TAT':<10}{'WT':<10}")
for r in completed:
    print(f"{r[0]:<8}{r[1]:<10}{r[2]:<10}{r[3]:<10}{r[4]:<10}{r[5]:<10}")
avg_wt=sum(r[5] for r in completed)/n
print(f"\nAverage waiting time:",avg_wt)