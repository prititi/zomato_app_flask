input=[
    {"name":"Emma", "designation":"develover", "salary":30000},
    {"name":"dipti", "designation":"manager", "salary":100000},
    {"name":"shivi", "designation":"develover", "salary":50000}
]

max=0;
temp= None;
for i in input:
    if i["salary"] > max:
        ans=i
print(ans)