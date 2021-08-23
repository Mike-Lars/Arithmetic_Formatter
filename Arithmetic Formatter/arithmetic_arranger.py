problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 1"]

lineDictionary = dict()

line1List = list()
line2List = list()
line3List = list()
line4List = list()

line1FormatString = ''
line2FormatString = ''
line3FormatString = ''
line4FormatString = ''

counter = 0

for problem in problems:
    items = problem.split()
    
    line1List.append(items[0])
    lineDictionary['line1'] = line1List
    
    longestItem = 0
    for item in items:
        if len(item) > longestItem:
            longestItem = len(item)
            
    line2Spacing = (longestItem + 2) - (len(items[2]) + 1)
    line2List.append(items[1] + (' ' * line2Spacing) + items[2])
    lineDictionary['line2'] = line2List
    
    line3List.append('-' * (longestItem + 2))
    lineDictionary['line3'] = line3List
    
    answer = None
    if items[1] == '+':
        answer = int(items[0]) + int(items[2])
    elif items[1] == '-':
        answer = int(items[0]) - int(items[2])
    line4List.append(str(answer))
    lineDictionary['line4'] = line4List
    
    relativeFormatPosition = longestItem + 6
    counter += 1
    if counter == 1:
        line1FormatString += '{:>' + str(longestItem + 2) + '}'
        line2FormatString += '{:>' + str(longestItem + 2) + '}'
        line3FormatString += '{:>' + str(longestItem + 2) + '}'
        line4FormatString += '{:>' + str(longestItem + 2) + '}'
    else:
        line1FormatString += '{:>' + str(longestItem + 6) + '}'
        line2FormatString += '{:>' + str(longestItem + 6) + '}'
        line3FormatString += '{:>' + str(longestItem + 6) + '}'
        line4FormatString += '{:>' + str(longestItem + 6) + '}'
    
#         new_line1 = line1FormatString.format(line1[counter - 1])



    

# line1 = lineDictionary['line1']
# try:
#     new_line1 = line1FormatString.format(line1[0], line1[1], line1[2], line1[3], line1[4])
# except:
#     pass

# line2 = lineDictionary['line2']
# try:
#     new_line2 = line2FormatString.format(line2[0], line2[1], line2[2], line2[3], line2[4])
# except:
#     pass

# line3 = lineDictionary['line3']
# try:
#     new_line3 = line3FormatString.format(line3[0], line3[1], line3[2], line3[3], line3[4])
# except:
#     pass

# line4 = lineDictionary['line4']
# try:
#     new_line4 = line4FormatString.format(line4[0], line4[1], line4[2], line4[3], line4[4])
# except:
#     pass

line1 = lineDictionary['line1']
new_line1 = line1FormatString.format(line1[0], line1[1], line1[2], line1[3], line1[4])

line2 = lineDictionary['line2']
new_line2 = line2FormatString.format(line2[0], line2[1], line2[2], line2[3], line2[4])

line3 = lineDictionary['line3']
new_line3 = line3FormatString.format(line3[0], line3[1], line3[2], line3[3], line3[4])

line4 = lineDictionary['line4']
new_line4 = line4FormatString.format(line4[0], line4[1], line4[2], line4[3], line4[4])

print(lineDictionary)
print()
print(line1List)
print(line2List)
print(line3List)
print(line4List)
print()
print(line1FormatString)
print(line2FormatString)
print(line3FormatString)
print(line4FormatString)
print()
print(new_line1)
print(new_line2)
print(new_line3)
print(new_line4)
