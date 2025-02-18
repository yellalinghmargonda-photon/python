def valid_parathesis(input_str):
    open_par=['{','[','(']
    temp_dict={}
    temp_dict['{']='}'
    temp_dict['['] = ']'
    temp_dict['('] = ')'
    temp=[]
    for i in input_str:
        if i in open_par:
          temp.append(i)
        else:
            if len(temp)>0:
                item=temp.pop()
                if i !=temp_dict[item]:
                    return False
            else:
                return  False
    return len(temp)==0
print(valid_parathesis("){"))

