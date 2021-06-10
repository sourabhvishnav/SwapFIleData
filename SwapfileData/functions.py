

def swapFileData() :
  fileName = input('Enter The File Name : ')
  fileName2 = input('Enter the second file : ')


  file1 = open(fileName , 'r')
  file1Data = file1.read()

  file2 = open(fileName2, 'r')
  file2Data = file2.read()
  
  file1 = open(fileName, 'w')
  file1.write(file2Data)

  file2 = open(fileName2, 'w')
  file2.write(file1Data)

swapFileData()