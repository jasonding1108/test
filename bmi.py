height = input ('input height(cm):')
weight = input ('input weight(kg):')

height = float(height)
weight = float(weight)

height = height / 100  #; cm transfer to m
bmi = weight / height / height

if bmi < 18.5:
	print('your BMI is', bmi, 'Underweight')
elif bmi >= 18.5 and bmi < 24:
	print('your BMI is', bmi, 'Normal')
elif bmi >= 24 and bmi < 27:
	print('your BMI is', bmi, 'Slightly heavier')
elif bmi >= 27 and bmi < 30:
	print('your BMI is', bmi, 'Mild obesity')
elif bmi >= 30 and bmi < 35:
	print('your BMI is', bmi, 'Moderate obesity')
else:
	print('your BMI is', bmi, 'Severe obesity')