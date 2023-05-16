import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('Intersections & Connections.xlsx', skiprows=0)

def exclude_empty_cells(row):
    return [value for value in row[2:9] if not pd.isna(value)]

# Create an empty dictionary to store the data
my_dict = {}

# Iterate over the rows of the DataFrame and populate the dictionary
for index, row in df.iterrows():
    key = row['Intersection']
    values = exclude_empty_cells(row)
    my_dict[key] = values

# Test to see that the data is true.
def test_my_dict():
    """
    runs through the dictionary to check if the values at each key reciprocate
    """
    fault_at = []
    Double = 0
    Incon = 0 
    count = 0
    good = 0
    for key in my_dict:
        test = key
        for i in my_dict[test]:
            # print (test)
            # print (i)
            count += 1
            if i == my_dict[test]:
                fault_at.append(f"node: {test} has a value error: {i}   ")
                Double += 1
                
            elif test in my_dict[i]:
                good += 1
                #print (f"node: {test}") 
                #print(f"Value: {i}")
                #print (f"Values at node {i}: {my_dict[i]}")
                
            else:
                fault_at.append(f"node: {test} has value: {i} but node: {i} does not have value: {test}   ")
                Incon += 1

    print (f"Error Count = {Double} Doubles and {Incon} Inconsistencies ")
    #print(count)
    return fault_at
# Print the resulting dictionary
##print(my_dict)

# Print the node errors 
print(test_my_dict())