obj = {}

str_type = (str(type(obj)).split()[1])
print('str_type = ', str_type)
str_type_class = str_type[0:len(str_type)-1]
print('len str_type_class = ', len(str_type_class))
print('len dict = ', len('dict'))

if str_type_class != "'dict'":
    print('TEST')

print('RRRRR = ', str_type_class)