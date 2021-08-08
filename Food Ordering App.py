#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Food:
    
    users= {}
    current_user = {}
    list_of_food=[ "tandoori chicken (4 pieces) [INR 240]","vegan burger (1piece)[INR 320]","traffle cake (500gm)[INR 900]"]
    food_info={"101":{"Name":"tandoori chicken","Quantity": " 4 pieces","Price":240,"Discount":0,"stock left":0},
            "102":{"Name":"vegan burger","Quantity":"1 piece","Price":320,"Discount":0,"stock left":0},
             "103":{"Name":"traffle cake","Quantity":"500 gram","Price":900,"Discount":0,"stock left":0}}

    
    def signup(self):
            self.users[len(Food.users) + 1] = {
            "name": input("Enter the name:"),
            "mobile": input("Enter the mobile:"),
            "email_id": input("Enter the email:"),
            "password": input("Enter the password:"),
            "type": input("Enter user_type:"),
            }
            print('User Registered Successfully')
            print(self.users)
            
    def login(self,email_id,user_password):
        for i in self.users:
#             print(self.users[i]['email_id'])
            if email_id == self.users[i]['email_id'] and user_password == self.users[i]['password']:
                print("Borrower is Logged in")
                self.current_user = self.users[i] 
                return self.current_user
        print('Wrong credentials')
        
    def menu(self):
        
        print('Please select any item from the menu:')
        
        print('press 1 to view list of food items:')
        print('press 2 to place a new order:')
        print('press 3 to view the order history:')
        print('press 4 to update profile:')
        action= int(input('your input   :'))
        
        if action == 1:
            print(self.food_info)
        
        if action ==2:
            Food.order(self)
                
        if action ==3:
            Food.show_order(self)
                
    def order(self):
        self.list_of_order=[]
        for i in range(len(self.list_of_food)):
            print("enter",i+1,"for",self.list_of_food[i])
        z=list(map(int,input().split(" ")))
        for i in z:
            print("You have selected ",self.list_of_food[i-1])
        print("Do you want to place your order? enter OK to place your order")
        if(input()=="OK"):
            for i in z:
                self.list_of_order.append(self.list_of_food[i-1])
            print("Your order has been placed,Enjoy your meal")
        else:
            return
        
    def show_order(self):
        print(self.list_of_order)
            
    def update_profile(self):
        print("NAME",self.name)
        print("DOB",self.dob)
        print("contact",self.contact)
        print("Email id",self.email)
        print("Password",self.password)
        x=input("what do you want to update")
        if(x=="NAME"):
            name= self.NAME()
            print("profile updated")
        elif(x=="DOB"):
            dob= self.DOB()
            print("profile updated")
        elif(x=="contact number"):
            contact=self.contact_num()
            print("profile updated")
        elif(x=="email Id"):
            email= self.email()
            print("profile updated")
        elif(x=="password"):
            Password=self.password()
            print("profile updated")
        else:
            print('You have not selected anythng to be updated')
        
    


# In[ ]:




