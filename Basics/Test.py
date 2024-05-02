name = ['Harry', 'Berry', 'Tina', 'Harsh']
score = [5, 37.21, 37.2, 39]
data = [[i, j] for i, j in zip(name, score)]
for i in range(0, len(data)):
    lownum = round(score[-2])
    scores = round(data[i][1])
    if scores == lownum:
        print(data[i][0])
