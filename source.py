
import random
import time

tables = [[],[]]

for j in range(0,2):
    for i in range(0, random.randint(1000000,1000000)):
        value = random.randint(-100,100)
        tables[j].append(value)

def functionOn2(table):
    start=0
    end=0
    sum=-100
    for i in range(0,len(table)):
        tempsum=0
        for j in range(i,len(table)):
            tempsum += table[j]
            if(tempsum>sum):
                sum = tempsum
                start = i
                end = j
    return [sum,start,end]

def functionOn3(table):
    start=0
    end=0
    sum=-100
    for i in range(0,len(table)): 
        for j in range(i,len(table)):
            tempsum=0
            for k in range(i,j+1):
                tempsum += table[k]
                if(tempsum>sum):
                    sum = tempsum
                    start = i
                    end = j
    return [sum,start,end]

def functionOn(table):
    start=0
    end=0
    tempstart=0
    tempsum=table[0]
    sum = tempsum
    for i in range(1,len(table)):
        if(tempsum>0):
            tempsum = table[i]+tempsum
        else:
            tempstart = i
            tempsum = table[i]
        
        if(tempsum>sum):
            sum = tempsum
            end = i
            start = tempstart
    return [sum,start,end]

def maxCrossingSum(table,begin,mid,end):
    tempsum = 0
    left_sum = -10000
    tempstart=mid
    tempend=mid

    for i in range(mid, begin-1, -1):
        tempsum += table[i]
        if(tempsum>left_sum):
            left_sum=tempsum
            tempstart=i

    tempsum=0
    right_sum=-10000
    for i in range(mid,end+1):
        tempsum+=table[i]
        if(tempsum>right_sum):
            right_sum = tempsum
            tempend = i
    
    combinedsum = left_sum+right_sum - table[mid]

    if(left_sum>combinedsum and left_sum>right_sum):
        tempend = mid
    if(right_sum>combinedsum and right_sum>left_sum):
        tempstart = mid

    return [max(combinedsum,left_sum,right_sum),tempstart,tempend]
  
   
def maxSubArraySum(table, begin, end): 
    if (begin > end): 
        return [-10000,0,0]
    if (begin == end): 
        return [table[begin],begin,end]
    m = (begin + end) // 2

    start=0
    ending = 0

    left = maxSubArraySum(table, begin, m-1)
    right = maxSubArraySum(table, m+1, end)
    cross = maxCrossingSum(table, begin, m, end)
    

    if(left[0]>cross[0] and left[0]>right[0]):
        start = left[1]
        ending = left[2]
    elif(right[0]>cross[0] and right[0]>left[0]):
        start = right[1]
        ending = right[2]
    else:
        start = cross[1]
        ending = cross[2]
    return [max(left[0],right[0],cross[0]),start,ending]
    
for table in tables:
    
    print(len(table))
  
    start_time=time.time()
    result = functionOn3(table)
    endtime = time.time()-start_time
    print("On^3 time %s seconds"%(endtime)+" time compared to size %s"%(endtime/len(table)))
    print(result)

    start_time=time.time()
    result = functionOn2(table)
    endtime = time.time()-start_time
    print("On^2 time %s seconds"%(endtime)+" time compared to size %s"%(endtime/len(table)))
    print(result)
   
    start_time=time.time()
    result=maxSubArraySum(table,0,len(table)-1)
    endtime = time.time()-start_time    
    print("Onlogn time %s seconds"%(endtime)+" time compared to size %s"%(endtime/len(table)))
    print(result)

    start_time=time.time()
    result=functionOn(table)
    endtime = time.time()-start_time
    print("On time %s seconds"%(endtime)+" time compared to size %s"%(endtime/len(table)))
    print(result)
