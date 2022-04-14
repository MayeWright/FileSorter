
toSort = open("ToSort\\SortMe.txt", "r")
sortArr = toSort.read().splitlines()
toSort.close()
open("Output\\Output.txt", "w").close()
output = open("Output\\Output.txt", "a")

check = 0

while check < 1:
    mode = input("Enter F to sort the file forwards alphabetically, R to sort backwards alphabetically,\n or T to run the test on the sort")
    if mode == 'F' or mode == 'R' or mode == 'T':
        check = 1
        
if mode == 'F':
    sortArr.sort()
elif mode == 'r':
    sortArr.sort(reverse=True)
else:
    toSort = open("Test\\TestTextUnsorted.txt", "r")
    sortForwardArr = toSort.read().splitlines()
    toSort.close()
    toSort = open("Test\\TestTextUnsorted.txt", "r")
    sortBackwardArr = toSort.read().splitlines()
    toSort.close()
    ForwardSorted = open("Test\\TestTextForward.txt", "r")
    ForwardSortedArr = ForwardSorted.read().splitlines()
    ForwardSorted.close()
    BackwardSorted = open("Test\\TestTextBackward.txt", "r")
    BackwardSortedArr = BackwardSorted.read().splitlines()
    BackwardSorted.close()

    sortForwardArr.sort()
    sortBackwardArr.sort(reverse=True)

    print("The Forward sort \n")
    if sortForwardArr == ForwardSortedArr:
        print("working")
    else:
        print("not working")

    print("The Backward sort \n")
    if sortBackwardArr == BackwardSortedArr:
        print("working")
    else:
        print("not working")


for elements in sortArr:
    output.write(elements)
    output.write("\n")
output.close()
