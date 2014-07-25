# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Copyright © 2010 Andreas Theodosiou. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
 

# Filename: unity.py
# Author: Andreas Theodosiou
# Description: A tool that accepts a quantity in a certain unit, and outputs that quantity in a number of other units.

import sys, string, decimal

# Units will store the units supported by unity, entity in which they belong
# and the conversion rate which will be used to convert them to the base unit
# for that entity.

units = {'m/s': ('speed', 1.0), 'km/h': ('speed', 0.2777777777777778), 'mph': ('speed', 0.44704), 'kn': ('speed', 0.5144), 'm': ('length', 1), 'ft': ('length', 0.3048), 'in': ('length', 0.0254), 'cm': ('length', 0.01), 'mm': ('length', 0.001)} 

# Generate the units dictionary using the Decimal data type instead of float.
units = {keys:(value1, decimal.Decimal(value2)) for keys, (value1, value2) in units.items()}

# get_quantity() will attempt to get the first argument from the command line, if there is any and convert it to a Decimal.
def get_quantity():
    try:
        quantity_test = decimal.Decimal(sys.argv[1])
        quantity = quantity_test
        return quantity
    except:
        quantity_test = sys.argv[1]
        if quantity_test == "about":
            print("Unity V0.5")
            sys.exit()
        else:
            print('Usage unity.py [quantity] [unit]')
            print('In other words you are using unity wrong')
            sys.exit()

# get_unit(dic) gets the unit from the command line parameter, checks if it exists inside the dictionary dic, if it does it returns the unit as a string. If it does not
# informs the user that the unit used is not supported 
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

    except IndexError as error:
        print(error)
        print()
        print('Index error was probably caused because you did not enter a unit')
        sys.exit()

# New function for implementing cli interactive mode.
# interactive_get_data(dic) gets input for the user, splits the quantity and unit and returns them as a list.
def interactive_get_data(dic):
    while True:
        try:
            list = []
            line = input('Enter the your quantity and the unit: ')
            data_list = str.split(line)
            if not data_list:
                print('That is useless')
                continue
            elif str(data_list[0]) == 'help':
                print()
                print('''Hello unity is a simple humble unit converter. Input a number followed by a unit, and unity will output a list possible unit conversions''')
                print()
                continue
            elif str(data_list[0]) == 'about':
                print()
                print('Unity Version 0.5')
                print('Author: Andreas Theodosiou')
                print('Please report bugs at http://github.com/MajorBiscuit/Unity/issues')
                print()
                continue
            elif str(data_list[0]) == 'quit':
                print()
                print('Unity is going to bed')
                print('Goodbye')
                print()
                sys.exit()
            else:
                quantity_test = decimal.Decimal(data_list[0])
                quantity = quantity_test
                list.append(quantity)
                unit_test = str(data_list[1])
                if unit_test in dic:
                    unit = unit_test
                    list.append(unit)
                else:
                    print('The unit', unit_test, 'is not supported by unity')
                    continue
                if list:
                    return list
        except ValueError as error:
            print()
            print('Input [quantity) [unit)')
            print(error)
            continue

        except IndexError as error:
            print(error)
            print()
            print('Index error was probably caused because you did not enter a unit')
            continue

# get_entity(unity, dic) finds what kind of quantity the input is and returns it.
def get_entity(unit, dic):
    entity = dic[unit][0]
    return entity

# convert_to_base(quantity, unit, dic) finds the entry for the unit received by the user inside the dictionary and uses its conversion to base unit rate to convert it to a base unit.
def convert_to_base(quantity, unit, dic):
    conversion_rate = dic[unit][1]
    base_unit = quantity * conversion_rate
    return base_unit

# generate_unit_conversion_list() generates the conversion list using the units dictionary. It removes the unit used by the user from the list and the units which do not belong to the same entity as the unit entered by the user.
def generate_unit_conversion_list():
    units_list = list(units.keys())
    units_list.remove(original_unit)
    return [unit for unit in units_list if units[unit][0] == entity]

# run_conversion(base_quantity, unit_conversion_list)) converts the original quantity into the appropriate units.
def run_conversion(base_quantity, unit_conversion_list):
	for unit in unit_conversion_list:
		converted_quantity = round(base_quantity * (1/units[unit][1]), 3)
		print(converted_quantity, unit)
		
# Check if there are arguments passed when running the apllication.
if len(sys.argv) < 2: #No arguments
    print('No command line arguments found, entering interactive mode')
    while True:
        original_quantity, original_unit = interactive_get_data(units) # Get input from the user
        entity = get_entity(original_unit, units)  # Find the type of quantity of the input
        base_quantity = convert_to_base(original_quantity, original_unit, units) # Convert to the base unit for that quantity
        unit_conversion_list = generate_unit_conversion_list() # Generate the list of appropriate units for the converion at hand.

        print()
        print('Input:', original_quantity, original_unit)
        print('Interpretation', entity)
        print('Unit conversions:')

        run_conversion(base_quantity, unit_conversion_list) # Run the conversion proccess and print the results
        print()

# In case there were arguments, get quantity and unit from command line arguments and repeat the process of converting.
else:
    original_quantity = get_quantity()
    original_unit = get_unit(units)
    entity = get_entity(original_unit, units)
    base_quantity = convert_to_base(original_quantity, original_unit, units)
    unit_conversion_list = generate_unit_conversion_list()


    print()
    print('Input:', original_quantity, original_unit)
    print('Interpretation', entity)
    print('Unit conversions:')

    run_conversion(base_quantity, unit_conversion_list)

