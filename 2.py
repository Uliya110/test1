its = 'kjabdshfkjadsh askdjhfkjadshf kajdshfjq'

raspred = {}

for i in its:
    if i in raspred.keys():
        raspred[i] += 1
    else:
        raspred[i] = 1
        
print(raspred)

its = 'kjabdshfkjadsh askdjhfkjadshf kajdshfjq'

raspred = {}

for i in its:
    if i not in raspred.keys():
        raspred[i] = its.count(i)
        
print(raspred)
print('hello!')


   
