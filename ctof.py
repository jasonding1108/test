
#user input C transfer to F
#F = C * 9/5 + 32

temp_c = input ('please input temperature (degree c):')
temp_c_float = float(temp_c)

temp_f = temp_c_float * 9/5 + 32
print('degree f is', temp_f)