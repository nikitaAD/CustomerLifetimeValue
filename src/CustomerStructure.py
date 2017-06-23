"""
Event is the parent class. Hold the customer_id and event_time.
Customer, SiteVisit, ImageUpload and Order are children of Event class.
Setter and Getter methods for members of the classes respectively.
"""

class Event(object):
    
    def __init__(self, customer_id, event_time):
        self.customer_id = customer_id
        self.event_time = event_time
        
    def getCustomerId(self):
        return self.customer_id
    
    def getEventTime(self):
        return self.event_time
    
    def __str__(self):
        return "%s, %s" % (self.key, self.event_time)


class Customer(Event):

    def __init__(self, key, event_time, last_name, adr_city, adr_state):
        Event.__init__(self, key, event_time)
        self.last_name = last_name
        self.adr_city = adr_city
        self.adr_state = adr_state
    
    
    def getLastName(self):
        return self.last_name
    
    def getAdrCity(self):
        return self.adr_city
    
    def getAdrState(self):
        self.adr_state

    def __str__(self):
        return "%s, %s, %s" % (self.last_name, self.adr_city, self.adr_state)
    

class SiteVisit(Event):
    
    def __init__(self, page_id, event_time, customer_id, tags):
        Event.__init__(self, customer_id, event_time)
        self.page_id = page_id
        self.tags = tags
    
    def getPageId(self):
        return self.page_id
    
    def getTags(self):
        return self.tags
    
    def __str__(self):
        return "%s, %s" % (self.page_id, self.tags)
    

class ImageUpload(Event):
    
    def __init__(self, image_id, event_time, customer_id, camera_make, camera_model):
        Event.__init__(self, customer_id, event_time)
        self.image_id = image_id
        self.camera_make = camera_make
        self.camera_model = camera_model
    
    def getImageId(self):
        return self.image_id
    
    def getCameraMake(self):
        return self.camera_make
    
    def getCameraModel(self):
        return self.camera_model
    
    def __str__(self):
        return "%s, %s, %s" % (self.image_id, self.camera_make, self.camera_model)
    

class Order(Event):
    
    def __init__(self, order_id, event_time, customer_id, total_amount):
        Event.__init__(self, customer_id, event_time)
        self.order_id = order_id
        self.total_amount = total_amount
    
    def getOrderId(self):
        return self.order_id
    
    def getTotalAmount(self):
        return self.total_amount
    
    def __str__(self):
        return "%s, %s" % (self.order_id, self.total_amount)
