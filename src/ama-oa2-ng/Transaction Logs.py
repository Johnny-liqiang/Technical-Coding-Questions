from typing import List
def getFraudIds(logData: List[List[str]], threshold: int) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = [ ]
    mydict = {}

    for each_rows in logData:
        row = ''.join(each_rows)
        temp = row.split()
        
        if (temp[0] != temp[1]):
            if temp[0] in mydict:
                mydict[temp[0]] += 1
            if temp[1] in mydict:
                mydict[temp[1]] += 1
            else:
                mydict[temp[0]] = 1
                mydict[temp[1]] = 1
        else:
            if temp[0] in mydict:
                mydict[temp[0]] += 1
        temp = ""
        
    for key, value in mydict.items():
        if value >= threshold:
            res.append(key)
        
    #print (res)
    res.sort(key = int, reverse =True)
        
    return res

if __name__ == "__main__":
    threshold = int(input())
    logDataNum = int(input())
    logData = [[x for x in input()] for _ in range(logDataNum)]
    result = getFraudIds(logData, threshold)
    print(' '.join(result))
