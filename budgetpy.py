"""Playing with Baltimore FY2021 budget data"""
import csv
########################
date_set = set()
agency_set = set()
service_set = set()
spending_category_set = set()
spending_description_set = set()
fund_set = set()
amount_set = set()
vendor_name_set = set()
name_set = set()
########################
date_amt = {}
agency_amt = {}
service_amt = {}
spending_category_amt = {}
spending_description_amt = {}
fund_amt = {}
amount_amt = {} # lol
vendor_name_amt = {}
name_amt = {}
########################
with open("Open_Checkbook_FY2021_Dataset.csv",'r',encoding='utf-8') as budget_file:
  reader = csv.reader(budget_file)
  next(reader)
  for row in reader:
    ########################
    date = row[2]
    agency = row[3]
    service = row[4]
    spending_category = row[5]
    spending_description = row[6]
    fund = row[7]
    amount = row[8]
    if amount:
      amount = float(row[8])
    else:
      amount = 0
    #print(float(amount))
    vendor_name = row[9]
    name = row[11]
    ########################
    date_set.add(date)
    agency_set.add(agency)
    service_set.add(service)
    spending_category_set.add(spending_category)
    spending_description_set.add(spending_description)
    fund_set.add(fund)
    amount_set.add(amount)
    vendor_name_set.add(vendor_name)
    name_set.add(name)
    ########################
    #print('blah')
    if date_amt.get(date,0):
      date_amt[date] += amount
    else:
      date_amt[date] = amount
    if agency_amt.get(agency,0):
      agency_amt[agency] += amount
    else:
      agency_amt[agency] = amount
    if service_amt.get(service,0):
      service_amt[service] += amount
    else:
      service_amt[service] = amount
    if spending_category_amt.get(spending_category,0):
      spending_category_amt[spending_category] += amount
    else:
      spending_category_amt[spending_category] = amount
    if spending_description_amt.get(spending_description,0):
      spending_description_amt[spending_description] += amount
    else:
      spending_description_amt[spending_description] = amount
    if fund_amt.get(fund,0):
      fund_amt[fund] += amount
    else:
      fund_amt[fund] = amount
    if amount_amt.get(amount,0):
      amount_amt[amount] += amount
    else:
      amount_amt[amount] = amount
    if vendor_name_amt.get(vendor_name,0):
      vendor_name_amt[vendor_name] += amount
    else:
      vendor_name_amt[vendor_name] = amount
    if name_amt.get(name,0):
      name_amt[name] += amount
    else:
      name_amt[name] = amount
budget_file.close()
#for entry in catset:
#  print(entry)
########################
print(len(date_set))
print(len(agency_set))
print(len(service_set))
print(len(spending_category_set))
print(len(spending_description_set))
print(len(fund_set))
print(len(amount_set))
print(len(vendor_name_set))
print(len(name_set))
print('###################')
########################
#print(sorted(date_set))
#print(sorted(agency_set))
#print(sorted(service_set))
#print(sorted(spending_category_set))
#print(sorted(spending_description_set))
#print(sorted(fund_set))
#print(sorted(amount_set))
#print(sorted(vendor_name_set))
#print(sorted(name_set))
########################
total = 0
#for entry in sorted(name_set):
for entry in sorted(agency_set):
  current_amt = round(agency_amt[entry],2)
  print(str(entry) + ' ' + str(current_amt))
  total += current_amt

print('TOTAL: ' + str(round(total,2)))
