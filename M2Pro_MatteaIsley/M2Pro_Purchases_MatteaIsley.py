# -*- coding: utf-8 -*-

# Converting purchases program to a modulerized program
# 02-16-2024
# CSC-121 M2Pro - Purchases
# Mattea Isley



def get_info(item_number):
    print("\nItem", item_number)
    item_count = float(input("\nEnter count of item: "))
    item_cost = float(input("\nEnter unit cost for item: "))
    return item_count, item_cost




def calc_cost(count, unit_cost):
    return count * unit_cost




def display_results(total_cost, tax):
    print("\nTotal Cost (pre-tax): $", total_cost)
    print("\nSales Tax: $", tax)
    print("\nTotal Cost (with tax): $", total_cost + tax)













