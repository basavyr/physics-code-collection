#!/Users/robertpoenaru/.pyenv/shims/python
def Join(data_1, data_2):
    l1 = len(data_1)
    l2 = len(data_2)
    ret_data = []
    if(l1 >= l2):
        count = 0
        for x1 in data_1:
            ret_data.append(x1)
            try:
                ret_data.append(data_2[count])
            except IndexError:
                pass
            else:
                count = count + 1
        return ret_data
    else:
        count = 0
        for x2 in data_2:
            ret_data.append(x2)
            try:
                ret_data.append(data_1[count])
            except IndexError:
                pass
            else:
                count = count + 1
        return ret_data
    return 'NAN'
