
def song(verses,chorus):
    qw = []
    for i in verses:
        for j in i:
            qw.append(j)
        for k in chorus:
            qw.append(k)
    for l in chorus:
        qw.append(l)
    return tuple(qw)
        
        