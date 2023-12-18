import ipdb
from Restaurant import Restaurant 
from Customer import Customer
from Review import Review


# creates new instances of Customer
dennis =Customer("dennis", "irungu")
# mwangi =Customer("mark", "mwangi")
stanley =Customer("stanley", "muiruri")
magret =Customer("magret", "wambui")

# 
Customer.all
# dennis.find_by_name



restaurnat1=Restaurant("Five Star")

restaurnat2=Restaurant("Everywhere")

review1=Review(dennis,restaurnat1, 3)

# print the number of reviews a specific customer has made
print(review1.all_reviews)


# Review.customers


review2=Review(stanley,restaurnat2 ,2)
# print(review2.all_reviews)
# review2.all_reviews

for review in Review.all():
    print(f"Review Rating: {review.rating}, Customer Data: {review._customer.__dict__}, Restaurant Data: {review._restaurant.__dict__}")


  

# ipdb.set_trace()