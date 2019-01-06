#create winning losing teams, find cosine similarity
file = open('trainingdata.txt').readlines()
winning_list = []

for line in file:
    line = line.strip().split(',')
    if line[-1] == 1:
        winning_list.append({'w': set(line[0:5]),'l': set(line[5:10])})
    else:
        winning_list.append({'w': set(line[5:]),'l': set(line[0:5])})

test = open('testingdata.txt').readlines()
N = int(test[0])
opt = open('output.txt', 'w+')
for i in range(1,N+1):
    sim1 = 0
    sim2 = 0

    set1 = set(test[i].split(',')[0:5])
    set2 = set(test[i].split(',')[5:])
    for entry in winning_list:
        sim1 = max(sim1, len(set1.intersection(entry['w']))+len(set2.intersection(entry['l'])))
        sim2 = max(sim2, len(set2.intersection(entry['w']))+len(set1.intersection(entry['l'])))

    diff = sim1 - sim2
    ans = (1 if diff>0 else 2)
    opt.write(str(ans)+'\n')

opt.close()