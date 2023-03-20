""" file1.txt
3
6
5
8
33
12
7
4
72
2
42
13
"""
""" file2.txt
3
6
13
5
7
89
12
3
33
34
1
344
42
"""



with open("file1.txt") as file1:
    file1_list = file1.readlines()
    file1_list = [int(num.replace('\n', '')) for num in file1_list]
    #print(file1_list)
    with open("file2.txt") as file2:
        file2_list = file2.readlines()
        file2_list = [int(num.replace('\n', '')) for num in file2_list]
        #print(file2_list)
        result = [num for num in file1_list if num in file2_list]





# Write your code above 👆

print(result)


