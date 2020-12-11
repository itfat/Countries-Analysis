
import csv
import matplotlib.pyplot as plt

with open('Gapminder.csv', 'r') as myFile:
    data = list(csv.reader(myFile, delimiter=','))
    # print(data)

def dataTypeConversion(rawList, dataType):
    convertedList = []
    previousValue = 0
    for item in rawList:
        if item != '':
            convertedList.append(dataType(item))
            previousValue = dataType(item)
        else:
            convertedList.append(previousValue) # replacing missing value with previous value
    return convertedList

def fetchIndices(data, columnIndex, searchItem):
    listRowIndices = []

    for i in range(len(data)):
        if data[i][columnIndex] == searchItem:
            listRowIndices.append(i)
            # print("Row indices include")
            # print(listRowIndices)
    
    return listRowIndices

def fetchColumnData(data, columnIndex, hasHeader):
    listData = []

    for i in range(len(data)):
        listData.append(data[i][columnIndex])
    if hasHeader:
        return listData[1:]
    else:
        return listData
    # print("List data is ")
    # print(listData)

def fetchData(data, columnIndex, listRowIndices):
    listDataValues = []

    for i in range(len(listRowIndices)):
        listDataValues.append(data[listRowIndices[i]][columnIndex])
       


    return listDataValues


paksitanIndices = fetchIndices(data,0,'Pakistan')
# print(paksitanIndices)
years = dataTypeConversion(fetchData(data,4,paksitanIndices),int)
# print(years)
countries = set(fetchColumnData(data,0,True))
# print(countries)
indicators = data[0][6:]
# print(indicators)
countriesDict = {}

for countryName in countries:
    countryIndices = fetchIndices(data,0,countryName)
    # print("Country indeces are")
    # print(countryIndices)
    for indicatorName in indicators:
        countriesDict[(countryName,indicatorName)] = dataTypeConversion(fetchData(data,data[0].index(indicatorName),countryIndices),float)

# print(sum(countriesDict[('Norway','AgriculturalLand')])/len(years))


# print("Length of years is")
# print(len(years))
# print(sum(countriesDict[('Norway','AgriculturalLand')]))
# print(indicators)
# print("Length of indicators is: ")
# print(len(indicators))
# print("Length of countries is: ")
# print(len(countries))

#print(len(countriesDict[('Pakistan','Taxrevenue')]))
result=[]
for i in countries:
    res=[]
    for j in indicators:
        res.append(sum(countriesDict[(i,j)])/len(years))
    result.append(res)
# print(len(res))
# print(len(result))
# # Making transpose of result do that we can get transpose and sort correctly
trans_ind=[]
for i in indicators:
    trans_count=[]
    for j in countries:
        trans_count.append(sum(countriesDict[j,i])/len(years))
    trans_ind.append(trans_count)

# # loaded the n/p indicator file here
import resulted_data
np_data=resulted_data.data
# print (np_data)

# # making copy of 2D array
new_array = map(list, result)
# print(new_array)
    # print(res)
    # print(len(res))
    # break
# print(type(result))
# print(len(result))
for i in trans_ind:
    i.sort()
    # print(i)
    
# print(trans_ind)

# # Comparison of two nested list to extract a country's name
countries=list(countries)
# print(countries)
# print(type(countries))
count_list=[]
for i in range(0,49):
    list_list=[]
    for j in range(0,227):
        for k in range(0,227):
            if(trans_ind[i][j]==result[k][i]):
                result[k][i]=-100
                list_list.append(countries[k])
#     print(count_list[i])
#     print("\n")
    count_list.append(list_list)
#     print(len(list_list))
# print(len(count_list))
# for i in range(len(count_list)):
#     print(count_list[i])
#     print("\n")
# i=0
# count=0
# for j in range(0,227):
#     for k in range(0,227):
#         # print(trans_ind[i][j])
#         # print("----------------------")
#         # print(new_array[k][i])
#         if(trans_ind[i][j]==result[k][i]):
#             count=count+1
#             print(j)
#             break
# print(count)




# type(countriesDict[i,j]/len(years))
# type(result)



# for indicatorName in indicators:
#     plt.figure()
#     plt.plot(years, countriesDict[('Pakistan',indicatorName)], 'green', label="Pakistan")
#     plt.plot(years, countriesDict[('India',indicatorName)], 'red', label="India")
#     plt.plot(years, countriesDict[('United States of America',indicatorName)], 'blue', label="USA")
#     plt.plot(years, countriesDict[('China',indicatorName)], 'black', label="China")
#     plt.plot(years, countriesDict[('Somalia',indicatorName)], 'orange', label="Somalia")
#     plt.plot(years, countriesDict[('Bangladesh',indicatorName)], 'yellow', label="Bangladesh")
#     plt.plot(years, countriesDict[('United Kingdom',indicatorName)], 'cyan', label="UK")
#     plt.plot(years, countriesDict[('Norway',indicatorName)], 'magenta', label="Norway")
#     plt.plot(years, countriesDict[('Kuwait',indicatorName)], 'purple', label="Kuwait")
#     plt.title(indicatorName)
#     plt.legend(loc="best")

# plt.show()




# For creatin a new file

# f= open("marked_data.txt","w+")
# f.write(str(indicators))
# f.close()

# # Importing n/p file to sort countires in asc or desc order
from resulted_data import data
j=0
for i in indicators:
    if(data[i]=='n'):
        count_list[j].reverse()
    j=j+1

# print(count_list[1])
# # Assigning rank by making csv file
# import csv

# with open('countries_rank.csv', mode='w') as countries_rank:
#     rank_writer = csv.writer(countries_rank, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     rank_writer.writerow([])
    
    # for i in indicators:
    #     for j in countries:
    #         rank_writer.writerow([i,j,
    #         count_list.index(i)])
    # rank_writer.writerow([])
    # rank_writer.writerow(['Erica Meyers', 'IT', 'March'])
index_list=[]
for j in countries:
    small=[]
    for i in count_list:
        small.append(i.index(j))
    # print(len(small))
    index_list.append(small)
# print(len(index_list))
# # collective final rank
final_rank=[]
for i in range(0,227):
    rank=0
    for j in range (0,49):
        rank=rank+index_list[i][j]
    final_rank.append(rank/49) 
# print(final_rank)
# # transponse of above
import numpy as np
numpy_array = np.array(index_list)

transpose = numpy_array.T

transpose_list = transpose.tolist()

# print(transpose_list[4])
# print(type(transpose_list))

my_file=open("result_rank.csv","w")
# my_file.write(','.join(countries))
my_file.write('{},{}'.format("IndicatorName",countries))
my_file.write("\n")
j=0
for k in indicators:
        my_file.write('{},{}'.format(k,transpose_list[j]) )
        my_file.write("\n")
        j=j+1
    
my_file.write('{},{}'.format("TotalRank",final_rank))
my_file.close()

# for i in countries:
#     print(i)
# for i in indicators:
#     for j in countries:
#         print(list_list.index([j]))
# print(list_list.index("Canada"))
# print(list_list.index("Pakistan"))


# # Add their indices and you are done
