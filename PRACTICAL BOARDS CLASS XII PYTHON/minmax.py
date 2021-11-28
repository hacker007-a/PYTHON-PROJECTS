# def largestsmallest(l):
#     s = l.sort()
#     min = l[0]
#     max = l[-1]
#     return max, min

# li = [12,34,668,3,20,888,100,198,45]
# l,m = largestsmallest(li)
# ui = input('Choose l for largest, m for smallest: ')
# if ui in 'Ll':
#     print(l)
# else:
#     print(m)

# [4,5,6,7,9,10]

def largestsmallest(l):
    min = l[0]
    max = l[0]
    for i in l:
        if min > i:
            min = i
    
        if max < i:
            max = i

    return min,max


li = [12,34,668,3,20,888,100,198,45]
m,l = largestsmallest(li)
ui = input('Choose l for largest, m for smallest: ')
if ui in 'Ll':
    print(l)
if ui in 'Mm':
    print(m)