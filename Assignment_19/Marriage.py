from random import randint
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
partner= [None for i in range(len(girls))]
result = [None for i in range(len(boys))]

i = 0
while partner[len(girls)-1] == None:
    indx = randint(0, len(girls)-1)
    if girls[indx] not in partner:
        partner[i] = girls[indx]
        i += 1

for i in range(len(boys)):
    result[i] = '('+ boys[i] +','+ partner[i] +')'   
print('result = ', result)