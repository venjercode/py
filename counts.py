str_x = "Emma is good developer. Emma is a writer.ok about ok.Emma is ok.Ema maybe ok"

s= str_x.lower()
s= s.replace('.', '').split()
print(s)



no=set()
yes=set()

for x in s:
    if x in no:
        yes.add(x)
        #print(yes)
    else:
        no.add(x)
        #print("no",no)
print("Total dupes:",yes)
