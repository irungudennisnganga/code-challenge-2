class Restaurant:
    def __init__(self, name):
        if type(name) == str :
            self.name = name
            #print(name)
        else:
            print("Enter valid data")    
    
    def name(self):
        return self.name
    

dennis =Restaurant('Five Star')
    
    
        