# Duy Le 1913048
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
oil_change = 35
tire_rotation = 19
car_wash = 7
car_wax = 12
print('')
service1 = input('Select first service:\n')
service2 = input('Select second service:\n')
print('')
print('Davy\'s auto shop invoice')
print('')
if service1 == 'Oil change' and service2 == 'Car wax':
    print('Service 1: Oil change, $35')
    print('Service 2: Car wax, $12')
    total = oil_change + car_wax
    print('')
    print('Total: $',total, sep = '')
if service1 == 'Tire rotation' and service2 == '-':
    print('Service 1: Tire rotation, $19')
    print('Service 2: No service')
    total2 = tire_rotation
    print('')
    print('Total: $',total2, sep = '')
if service1 == 'Tire rotation' and service2 == 'Car wash':
    print('Service 1: Tire rotation, $19')
    print('Service 2: Car wash, $19')
    total3 = tire_rotation + car_wash
    print('Total: $',total3, sep = '')