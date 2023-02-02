def unique(list):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    print(str(unique_list)[1:-1])
list = [1,2,3,3,3,3,4,5]
unique(list)