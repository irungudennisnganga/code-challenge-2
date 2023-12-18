from Restaurant import Restaurant

class Customer:
    all_customers =[]
    all_restaurants =[]
    
    def __init__(self, name, f_name):
        self.name = name
        self.f_name = f_name  
        self.full_names= f"{name } {f_name}"
        self.reviews = []
        Customer.all_customers.append(self.full_names)
        # self.all()
        
       
    
    
    def given_name(self):
        return self.name
            
    def family_name(self):
        return self.f_name   
    
    def full_name(self):
        return (f"{self.name} {self.f_name}")     
    
    @classmethod
    def all(cls):
        
        cls.all_customers
        # print([name for name in cls.all_customers])
       
    def restaurant(self):
        pass
        # print(list(set(review.restaurant() for review in Review.all() if review.customer() == self)))    
        
    def add_review(self):
        new_review = (Restaurant.name,3)
        self.reviews.append(new_review)
        
        # print([review for review in self.reviews])
        
        
    def num_reviews(self):
        return len(self.reviews)

    
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if cls.full_name == name:
                print (customer)
    print(None)

    
    
# dennis =Customer("dennis" , "irungu")   

# dennis.add_review() 

