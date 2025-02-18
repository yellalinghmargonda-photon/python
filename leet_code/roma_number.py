def roman_number(r_num : str)->int:
    number: int=0
    roman_to_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    for i in range(len(r_num)-1):
        
        temp=0
        if roman_to_value[r_num[i]]>roman_to_value[r_num[i+1]]:
            temp=roman_to_value[r_num[i]]
        if roman_to_value[r_num[i]]<roman_to_value[r_num[i+1]]:
            temp=roman_to_value[r_num[i+1]]-roman_to_value[r_num[i]]
            i+=1

        number=number+temp
        print(number)
    return number
num=roman_number("MCMXCIV")
print(num)

