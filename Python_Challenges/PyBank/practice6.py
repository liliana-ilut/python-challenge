#declare variables 
    months = [] 
    profit_loss = 0
    average_pl_change=0
    greatest_profit=[]
    greatest_loss= 0
    greatest = 0
    profit = []
    change = []
    for r in csv_reader:
        month = r[0]
        if month not in months:
            months.append(months)
        profit_loss += int(r[1])
        profit.append(r[1])
    for i in range(len(profit)-1):
        changes = int(profit[i+1]) - int(profit[i])
        if changes not in change:
            change.append(changes)
    greatest = max(change)    
    greatest_loss = min(change)
    for a in range(len(change)):
        if greatest == change[a]:
            print(months[a])
print('Total months = ' + str(len(months)))
print('Total P & L = ' + str(profit_loss))
print('Maximum Profit = ' + str(greatest))
print('Maximum Loss = ' + str(greatest_loss))
a= (int(profit[85])) - (int(profit[0]))
b= a/(len(months)-1)
print(b)