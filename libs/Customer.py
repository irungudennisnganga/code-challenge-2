class Customer:
    all_customers =[]
    
    def __init__(self, name, f_name):
        self.name = name
        self.f_name = f_name  
        full_names= f"{name } {f_name}"
        
        self.all(full_names) 
    
    
    def given_name(self):
        return self.name
            
    def family_name(self):
        return self.f_name   
    
    def full_name(self):
        return (f"{self.name} {self.f_name}")     
    
    @classmethod
    def all(cls, full_names):
        return cls.all_customers.append(full_names)
        #print([name for name in cls.all_customers])
        
    
    
dennis =Customer("dennis" , "irungu")   
 

