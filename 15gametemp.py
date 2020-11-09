import sys
#make root as string
root1 = sys.argv[1]
if(len(root1)==15):
    root1 = (root1, "_")
elif(len(root1)<15):
    root1 = (root1, "_", sys.argv[2])
root1 = ''.join(root1)
root1 = root1.replace('A', '1 ')
root1 = root1.replace('B', '2 ')
root1 = root1.replace('C', '3 ')
root1 = root1.replace('D', '4 ')
root1 = root1.replace('E', '5 ')
root1 = root1.replace('F', '6 ')
root1 = root1.replace('G', '7 ')
root1 = root1.replace('H', '8 ')
root1 = root1.replace('I', '9 ')
root1 = root1.replace('J', '10 ')
root1 = root1.replace('K', '11 ')
root1 = root1.replace('L', '12 ')
root1 = root1.replace('M', '13 ')
root1 = root1.replace('N', '14 ')
root1 = root1.replace('O', '15 ')
root = root1.split(' ')
print(root)