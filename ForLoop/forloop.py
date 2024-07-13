target_profit = 100000
jan_profit= 90000
feb_profit= 100000
mar_profit= 110000
apr_profit= 98000
may_profit =115000
june_profit = 105000

profit = [jan_profit, feb_profit, mar_profit, apr_profit, may_profit, june_profit]
months = ['January', 'February', 'March', 'April', 'May', 'June']
for (items, month) in zip(profit, months):
    if items > target_profit:
        print(f'The target was exceeded by {items - target_profit} in {month}')
    elif items == target_profit:
        print(f'The target and your profit are th same in {month}')
    else:
        print(f'You fell short by {target_profit - items} in {month}')