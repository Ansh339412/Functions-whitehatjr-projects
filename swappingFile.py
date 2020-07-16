def SwapFileData():
    fileOneData     =   input("Enter your file name :  ")
    fileTwoData     =   input("Enter your file name :  ")
    with open(fileOneData,'r') as sampleA:
        data_sampleA    =   sampleA.read()

    with open(fileTwoData, 'r') as sampleB:
        data_sampleB = sampleB.read()

    with open(fileOneData, 'w') as sampleA:
        data_sampleA.write(data_sampleB)

    with open(fileTwoData, 'w') as sampleB:
        data_sampleB.write(data_sampleA)

SwapFileData()
    
    
