import os
import json
import CustomerStructure

d = []
cust_list = []
site_visit_list = []
image_upload_list = []
order_list = []

"""
Function updates Customer
Parameter feature in Customer  will be updated with new_value
"""
def update_customer(key, feature, new_value):
        for customer in cust_list:
            if key == customer.key:
                customer.feature = new_value

"""
Function updates Order
Parameter feature in Order  will be updated with new_value
"""        
def update_order(key, feature, new_value):
        for order in order_list:
            if key == order.order_id:
                order.feature = new_value

"""
Parameter file will be parsed.
Data is stored as lists of Objects of respective classes in CustomerStructure
"""
def Ingest(fileName):
  #Reading file as json data
  try:
    with open(fileName,"r") as json_data:
        d = json.load(json_data)
  except:
    raise IOError("Can't open file %s for reading" % fileName)
  
  #Type and Verb from Data are matched and respective objects are created  
  try:
    for row in d:
        if "CUSTOMER" == row["type"] and "NEW" == row["verb"]:
            cust = CustomerStructure.Customer(row["key"], row["event_time"], row["last_name"], row["adr_city"], row["adr_state"])
            cust_list.append(cust)
        elif "CUSTOMER" == row["type"] and "UPDATE" == row["verb"]:
            update_customer(row["key"], row["last_name"], "Lincoln")
        elif "SITE_VISIT" == row["type"] and "NEW" == row["verb"]:
            site_v = CustomerStructure.SiteVisit(row["key"], row["event_time"], row["customer_id"], row["tags"])
            site_visit_list.append(site_v)
        elif "IMAGE" == row["type"] and "UPLOAD" == row["verb"]:
            image_u = CustomerStructure.ImageUpload(row["key"], row["event_time"], row["customer_id"], row["camera_make"], row["camera_model"])
            image_upload_list.append(image_u)
        elif "ORDER" == row["type"] and "NEW" == row["verb"]:
            ord = CustomerStructure.Order(row["key"], row["event_time"], row["customer_id"], row["total_amount"])
            order_list.append(ord)
        elif "ORDER" == row["type"] and "UPDATE" == row["verb"]:
            update_order(row["key"], row["total_amount"], "13 USD")
        else:
            print("Error in reading file")
  except ValueError:
    raise IOError("Error reading file %s at line:\n%s" % (fileName, row))
