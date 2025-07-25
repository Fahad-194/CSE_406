n=int(input("Enter number of Processes:"))
pros = []
for i in range(n):
    pid = f"P{i+1}"
    at = int(input(f"Enter arrival time for {pid}: "))
    bt= int(input(f"Enter burst time for: {pid}: "))
    pros.append([pid,at,bt])
for i in range(n):
    for j in range(i+1,n):
        if pros[i][1]>pros[j][1]:
            pros[i],pros[j]= pros[j],pros[i]
com_t=[]
tat=[]
wt=[]
current_t=0
for i in range (n):
    at=pros[i][1]
    bt=pros[i][2]
    if current_t < at:
        current_t=at
    current_t=current_t+bt
    com_t.append(current_t)
    tat.append(com_t[i]-at)
    wt.append(tat[i]-bt)
print(f"\n{'Process':<8}{'Arrival':<10}{'Burst':<10}{'CT':<10}{'TAT':<10}{'WT':<10}")
for i in range (n):
    print(f"{pros[i][0]:<8}{pros[i][1]:<10}{pros[i][2]:<10}{com_t[i]:<10}{tat[i]:<10}{wt[i]:<10}")
avg_wt=sum(wt)/n
print(f"\nAverage waiting time:",avg_wt)
