from Review import Review

class Customer:
    all_customers =[]
    all_restaurants =[]
    
    def __init__(self, given_name, f_name):
        self.name = given_name
        self.f_name = f_name  
        self.full_names= f"{given_name } {f_name}"
     
        self.all_customers.append(self.full_names)
       
        
        
    def given_name(self):
        return self.name
            
    def family_name(self):
        return self.f_name   
    
    def full_name(self):
        return f"{self.name} {self.f_name}"   
    
    @classmethod
    def all(cls):
        return cls.all_customers
        
        
       
    def restaurant(self):
        return list([set(review.restaurant() for review in Review.all())]) 
    
     
    # @classmethod  
    def add_review(self,restaurant, rating):
        new_review = restaurant,rating
        self.reviews.append(new_review)
        
        
        
    def num_reviews(self):
        return len([review for review in Review.all() if review.customers() == self])

    
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if cls.full_name == name:
                print (customer)
    print(None)

  




