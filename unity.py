#!/usr/bin/env python3
# Filename: unity.py
# Author: Andreas Theodosiou
# Description: A tool that accepts a quantity in a certain unit, and outputs
# that quantity in a number of other units.

import sys
import string

# Units will store the units supported by unity, entity in which they belong
# and the conversion rate which will be used to convert them to the base unit
# for that entity.

units = {'m/s': ['speed', 1.0], 'km/h': ['speed', 0.2778], 'mph': ['speed', 0.447], 'kn': ['speed', 0.5144], 'm': ['length', 1], 'ft': ['length', 0.3048]} 

# Entities will store all the units and conversion rates for those units of
# each entity.

entities = {'speed': [['m/s', 1], ['km/h', 3.6], ['mph', 2.237], ['kn', 1.944]], 'length': [['m', 1], ['ft', 3.281]]}

def get_quantity():
    try:
        quantity_test = float(sys.argv[1])
        if quantity_test >= 1:
            quantity = quantity_test
            return quantity
        else:
            print('You have to enter a number that is greater than zero')
    except ValueError:
        print('Usage unity.py [quantity] [unit]')
        print('In other words you are using unity wrong')
        sys.exit()

def get_unit(dic):
    try:
        unit_test = str(sys.argv[2])
        if unit_test in dic:
            unit = unit_test
            return unit
        else:
            print('The unit', unit_test, 'is not supported by unity')
    except ValueError:
        print('Usage unity.py [quantity] [unit]')
        sys.exit()

# New function for implementing cli interactive mode
def interactive_get_data(dic):
    while True:
        try:
            line = input('Enter the your quantity and the unit: ')
            data_list = str.split(line)
            if not data_list:
                print('That is useless')
                continue
            else:
                quantity_test = float(data_list[0])
                if quantity_test >= 1:
                    quantity = quantity_test
                    return quantity
                else:
                    print('You have to enter a number that is greater than zero')
                    continue
                unit_test = str(data_list[1])
                if unit_test in dic:
                    unit = unit_test
                    return unit
                else:
                    print('The unit', unit_test, 'is not supported by unity')
                    continue
        except ValueError as error:
            print('Input [quantity] [unit]')
            print(error)

def get_entity(unit, dic):
    entity = dic[unit][0]
    return entity

def convert_to_base(quantity, unit, dic):
    conversion_rate = dic[unit][1]
    base_unit = quantity * conversion_rate
    return base_unit
    
def format_conv_list(conv_list, unit):
    index = 0
    while index < len(conv_list):
        if unit in conv_list[index]:
            del conv_list[index]
            formatted_conv_list = conv_list
            return formatted_conv_list
            break
        else:
            index += 1
            continue

def print_conversion(conv_list, base_unit):
    index = 0
    while index < len(conv_list):
        unit = str(conv_list[index][0])
        rate = float(conv_list[index][1])
        converted_quantity = base_unit * rate
        print(converted_quantity, unit)
        index += 1


if len(sys.argv) < 2:
    print('No action specified')
    print('Terminating unity')
    sys.exit()

original_quantity = get_quantity()
original_unit = get_unit(units)
entity = get_entity(original_unit, units)
base_unit = convert_to_base(original_quantity, original_unit, units)
conversion_list = entities[entity]

formatted_conv_list = format_conv_list(conversion_list, original_unit)
#index = 0
#while index < len(conversion_list):
#    if original_unit in conversion_list[index]:
#        del conversion_list[index]
#        formatted_conversion_list = conversion_list
#        break
#    else:
#        index += 1
#        continue

print('Input:', original_quantity, original_unit)
print('Interpretation', entity)
print('Unit conversions:')

print_conversion(formatted_conv_list, base_unit)
#idx = 0 
#while idx < len(formatted_conversion_list):
#    unit = str(formatted_conversion_list[idx][0])
#    rate = float(formatted_conversion_list[idx][1])
#    converted_quantity = base_unit * rate
#    print(converted_quantity, unit)
#    idx += 1

