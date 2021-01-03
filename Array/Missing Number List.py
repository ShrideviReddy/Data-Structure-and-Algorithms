# Missing number from 1 to 100
def missingno(X):
    n = len(X)
    total = (n+1)*(n+2)/2
    sum_of_list = sum(X)
    return total - sum_of_list
missing_list = [1, 2, 4, 5]
missing_number = missingno(missing_list)
print("Missing no.", missing_number)
