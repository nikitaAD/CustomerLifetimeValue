import os
import Ingest
import TopXSimpleLTV

"""
Ingest function has a parameter for filepath/filename. 
Function definition in Ingest.py
It parses the file and populates the data based on event type for customer.
"""
Ingest.Ingest(os.path.join('..', 'input', 'input.txt'))


"""
TopXSimpleLTVCustomers function has 2 parameters:
	 number of customers to print to file
	 Data/order_list which is a list of instances of class Order
X customers with highest simpleLTV are written to output.txt
To test with sample_input data week of 2017/1/1 to 2017/1/7 is hard-coded. 
Function can be extended for bigger dataset
"""
TopXSimpleLTV.TopXSimpleLTVCustomers(10, Ingest.order_list)
