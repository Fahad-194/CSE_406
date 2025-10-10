pages=list(map(int,input("Enter page reference:").split()))
frame=int(input("Enter number of frame:"))
mem=[]
page_faults=0
for i in pages:
    if i not in mem:
        if len(mem)<frame:
            mem.append(i)
        else:
            mem.pop(0)
            mem.append(i)
        page_faults+=1
    else:
        mem.remove(i)
        mem.append(i)
    print(f"Page:{i}-->{mem}")
print(f"Total page fault:{page_faults}")
print(f"Page Hits:{len(pages)- page_faults}")