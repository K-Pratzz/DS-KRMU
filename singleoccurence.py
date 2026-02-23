arr=[1,2,5,6,5,3,2,3,6]
def singleOcuurence(arr):
    result=0
    for i in arr:
        result^=i
    return result
print(singleOcuurence(arr))