class Restaurant:
    restaurant =[]
    def __init__(self, name):
        if type(name) == str :
            self._name = name
            self.reviews_list = []
            Restaurant.restaurant.append(self)
            
        else:
            print("Enter valid data")    
    
    def name(self):
        return self._name
    
    def reviews(self):
        return self.review_list
    
    def customers(self):
        return list(set(review.customers() for review in self.reviews_list))
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum([review.rating for review in self.reviews])
        return total_rating / len(self.reviews)

    


    
        