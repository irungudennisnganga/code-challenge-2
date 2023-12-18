class Review:
    all_reviews =[]
    
    def __init__(self,customer, restaurant,rating):
        if type(rating) == int:
            self._customer = customer
            self._restaurant = restaurant
            self.rating = rating
            self.all_reviews.append(self)
            
        
       
        
    
    def rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    # @classmethod
    # def create_review(cls,customer,restaurant,rating):
    #     new_review =cls(customer,restaurant,rating)
    #     return cls.all_reviews.append(new_review)
        
    
    
    def customers(self):
       return self._customer
    
    def restaurant(self):
        return self._restaurant
        
        
        
