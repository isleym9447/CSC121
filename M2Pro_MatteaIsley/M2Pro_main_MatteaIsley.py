# -*- coding: utf-8 -*-


# Purchases
# 2-2-2024
# CSC121 M1Lab2– Review
# Mattea Isley



from M2Pro_Purchases_MatteaIsley import get_info, calc_cost, display_results

def main():
    total_cost = 0
    toal_tax = 0
    
    num_items = int(input("Enter the number of items: "))
    
    for item_num in range(1, num_items + 1):
        item_count, item_cost = get_info(item_num)
        total_cost += calc_cost(item_count, item_cost)

    tax_rate = float(input("\nEnter sales tax rate (%): "))
    tax = (total_cost * tax_rate) / 100
    display_results(total_cost, tax)

if __name__ == "__main__":
    main()