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
    
  
    def customers(self):
       return self._customer
    
    def restaurant(self):
        return self._restaurant
        
        
        
