#!/usr/bin/env python3

n = 3

# Task 2.1: Real score S = 3.914193, normalized total score is 0.740268
# Task 2.2: Real score S = 12.509336, normalized total score is 0.948987
# Task 2.3: Real score S = 61.396589, normalized total score is 0.994458
# Task 2.4: Requires optimization 

fi = open('../task2/input_'+str(n)+'.txt')
fo = open('../task2/task2.'+str(n)+'.test.txt','w')

t = int(fi.readline())
marks = []
for line in fi:
    marks.append(list(line.strip()))
fi.close()

df = pd.DataFrame(marks).T
perbasestates = pd.DataFrame(df.apply(''.join, axis=1))[0].tolist()
perbasestatecnts = [perbasestates.count(x) for x in perbasestates]
freq_states = sorted(a, key=Counter(a).get, reverse=True)


result = [freq_states.index(x)+1 if freq_states.count(x)>maxocc[t] else 0 for x in perbasestates]
stateids = sorted(list(set(result)))
result = [stateids.index(x) for x in result]
fo.write(' '.join(map(str,result))+'\n')
fo.close()