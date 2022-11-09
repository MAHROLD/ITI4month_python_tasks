##show list
# print("#"+"    "+"items"+"    "+"PRICE")
# count=1
# for keys, value in products.items():
   # print(str(count)+"    "+keys+"    "+str(products[keys]["cost"]))
   # count+=1
products={"apple":{"quantity":60,"cost":6},
         "orange":{"quantity":70,"cost":7},
         "mango":{"quantity":80,"cost":8}}
bill={"apple":{"quantity":0,"cost":0},
         "orange":{"quantity":0,"cost":0},
         "mango":{"quantity":0,"cost":0}}

def add_products():
    print("#"+"    "+"items"+"    "+"PRICE"+"    "+"quantity")
    count=1
    for keys, value in products.items():
        print(str(count)+"    "+keys+"    "+str(products[keys]["cost"])+"          "+str(products[keys]["quantity"]))
        count+=1
    newp_name=input("enter new product name: ")
    newp_cost=input("enter the cost of the product: ")
    newp_quantity=input("enter the stock level of the product: ")
    products.update({newp_name:{"quantity":newp_cost,"cost":newp_cost}})
    bill.update({newp_name:{"quantity":"0","cost":"0"}})

def show_product():
    print("#"+"    "+"items"+"    "+"PRICE"+"    "+"quantity")
    count=1
    for keys, value in products.items():
        print(str(count)+"    "+keys+"    "+str(products[keys]["cost"])+"          "+str(products[keys]["quantity"]))
        count+=1
def show_shopping():
    print("#"+"    "+"items"+"    "+"PRICE"+"    "+"quantity")
    count=1
    for keys, value in bill.items():
        print(str(count)+"    "+keys+"    "+str(bill[keys]["cost"])+"          "+str(bill[keys]["quantity"]))
        count+=1
    
def change_cost():
    show_product()
    nameofproduct=input("enter the name of the product : ")
    updated_cost=input("enter the updated cost : ")
    products.update({nameofproduct:{"quantity":(products[nameofproduct]["quantity"]),"cost":updated_cost}})
    
    
    
while 1:
    print("#Welcome to ITI Shop\n1- Customer\n2- Owner\n0- exit")
    op=input("Select Mode For customer press 1 , for owner press two , to exist press 0 :")  
    
    if op=="1":
        while 1:
        
            print("\n1- show our products ")
            print("2- Buy from our products ")
            print("3- print the bill ")
            print("0-to Exit")
            customer_choice=input("enter your choice: ")
            if customer_choice == "2": 
                show_product()
                buy_choice=input("for buy page press 1 : ")
                if buy_choice == "1":
                    buy_name=input("enter the product name : ")
                    buy_quantity=input("enter the quantity in KG : ")
                    bill.update({buy_name:{"quantity":buy_quantity,"cost":int((products[buy_name]["cost"])*int(buy_quantity))}})
                    products.update({buy_name:{"quantity":str(int(products[buy_name]["quantity"])-int(buy_quantity)),"cost":int((products[buy_name]["cost"])*int(buy_quantity))}})
                    
                    while input("press 1 to add more and 0 to stop adding prducts ")!="0":
                        buy_name=input("enter the product name : ")
                        buy_quantity=input("enter the quantity in KG : ")
                      
                        bill.update({buy_name:{"quantity":buy_quantity,"cost":int((products[buy_name]["cost"])*int(buy_quantity))}})
                        products.update({buy_name:{"quantity":str(int(products[buy_name]["quantity"])-int(buy_quantity)),"cost":products[buy_name]["cost"]}})
                    show_shopping()
              
                    continue
            if customer_choice == "1":
                show_product()
            if customer_choice == "3":
                show_shopping()
                total_cost=0
                total_cost=int(total_cost)
                for keys, value in products.items():
                    
                    total_cost=int(total_cost)+int(bill[keys]["cost"])
                    
                print("total cost = "+ str(total_cost))
                print("\nTHANK YOU FOR PURSCHING FROM OUR STORE\n")
            if customer_choice == "0": 
                break        
 
                  
            
            
                
                
	##Enter Password :1234
	##password wrong try again:12345	
    ##[for 3 iteration then exit to last board]
        continue
    if op=="2":
        user="muhammad"
        user=input("Enter User name: ")
        if user=="muhammad" or user=="Muhammad":
            pswd="1234"
            for i in range(3):
                if i==0:
                    pswd=input("Enter User Password: ")
                if i !=0:
                    pswd=input("wrong password enter the correct Password: ")
                if pswd == "1234":
                    break
                if pswd != "1234" and i==2:
                    break
            if pswd != "1234":
                continue
            while(1):
                print("\nWelcome back MR. "+str(user))
                print("\n1-Add new products")
                print("2-Show Products")
                print("3-Change cost")
                print("0-to Exit")
                owner_choice=input("enter your choice: ")
            
                if owner_choice == "1": 
                    add_products()
                    while input("to add more press 1 and 0 to exit: ")!="0":
                        add_products()
                    continue
                if owner_choice == "2": 
                    show_product()
                    continue
                if owner_choice == "3": 
                    change_cost()
                    while input("to change one more press 1 and 0 to exit: ")!="0":
                       change_cost()
                    continue
                if owner_choice == "0": 
                    break
        continue
    if op=="0":
        break
    print("incorrect input enter the correct operation")
