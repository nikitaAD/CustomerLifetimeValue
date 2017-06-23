import os
from datetime import datetime
import operator

#key=customer_id, value=total_expenditure
CustomersExpenditure = {}

#key=customer_id, value=num_of_visits
CustomersVisits = {}

#key=customer_id, value=SimpleLTV
CustomersSimpleLTV = {}

"""
Calculates simpleLTV for customers from the order_list
Top x customers SimpleLTV is written to Output.txt file
"""
def TopXSimpleLTVCustomers(x, order_list):
    for a in order_list:
	#using datetime to retrieve orders of 1 week. Here 2017/1/1 to 2017/1/7
        datetime_object = datetime.strptime(a.event_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        if 2017 == datetime_object.year and 1 == datetime_object.month and 1<datetime_object.day<7:
            if a.customer_id in CustomersExpenditure:
                order_amount = CustomersExpenditure.get(a.customer_id)
                CustomersExpenditure[a.customer_id] = order_amount + a.total_amount
                CustomersVisits[a.customer_id] += 1
            else:
                CustomersExpenditure[a.customer_id] = a.total_amount
                CustomersVisits[a.customer_id] = 1
    
    #Calculating SimpleLTV
    for k in CustomersExpenditure:
        amt = CustomersExpenditure[k].split()
        a = 52 * (float(amt[0]) * float(CustomersVisits.get(k))) * 10
        CustomersSimpleLTV[k] = a
    
    #Sorting SimpleLTV in descending order and writing top x to output file
    try: 
        sorted_x = sorted(CustomersSimpleLTV.items(), key=operator.itemgetter(1))
        for y in sorted_x[:x]:
            with open(os.path.join('..', 'output', 'output.txt'), 'a') as output_file:
                 output_file.write("Customer_id= {} : SimpleLTV= {}\n".format(y[0], y[1]))
    except:
        raise IOError("Can't open file %s for writing" % f)
