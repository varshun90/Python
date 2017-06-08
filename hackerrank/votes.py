def  electionWinner(votes):
    box={}
    for vote in votes:
        box[vote]=box.get(vote, 0) +1
    sortedbox=sorted(box.items(), key=lambda x: x[1], reverse=True)
    maxvote= sortedbox[0][1]
    names=[]
    for (name,vote) in sortedbox:
        if vote==maxvote :
            names.append(name)
    return sorted(names,reverse=True)[0]