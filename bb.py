import pyfiglet

word = 'Seo-jung'
ascii_1 = pyfiglet.figlet_format(word )
print(ascii_1)

print('Hello World! This is my first code. I am learning python')

# Yamaha 
yamaha_brand = ['motorcycle1', 'motorcycle2']
price_yamaha = [1000, 2000]

# Honda 
honda_brand = ['motorcycle3', 'motorcycle4']
price_honda = [3000, 4000]

# Suzuki 
suzuki_brand = ['motorcycle5', 'motorcycle6']
price_suzuki = [5000, 6000]

# Input for buyer's motorcycle
buyer_name = input('Enter your name: ')
buyer_id = input('Enter your ID: ')
buyer_dt = input('Enter date: ')

choose_brand = input('Enter brand: ')
choose_type = input(f'Enter type of {choose_brand}: ')
unit = input(f'Enter unit of {choose_type}: ')

# if choose_brand == 'yamaha' and choose_type == 'motorcycle1':


def list_motorcycle():
  print(f'''
  A. Yamaha
    1. Motorcycle1
    2. Motorcycle2
    
  B. Honda
    3. Motorcycle3
    4. Motorcycle4
    
  C. Suzuki
    5. Motorcycle5
    6. Motorcycle6
''')

list_motorcycle()
