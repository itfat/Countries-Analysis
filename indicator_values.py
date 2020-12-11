import marked_data;

# # input indicator list 
# # output dictionary with tuples of indicators and N/P values

my_list = marked_data.l
my_dict={}
for i in my_list:
    v = raw_input("Enter n/p for "+i+": ")
    my_dict.update({i: v})

f= open("resulted_data.txt","w+")
f.write(str(my_dict))
f.close()