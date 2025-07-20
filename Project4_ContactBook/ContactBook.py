Contact={}

def View_contact():
  if not Contact:
        print("Contact Book is Empty")
        return
  print(f"{'Name':<15}{'Phone':<15}{'Email':<25}{'Address':<30}")
  print("-" * 85)
  for name, details in Contact.items():
    print(f"{name:<15}{details['phone']:<15}{details['email']:<25}{details['address']:<30}")
def menu():
  while True:
    print("\n____MAIN MENU___")
    print("(1) Add a new Contact")
    print("(2) Search Contact")
    print("(3) View Contact List")
    print("(4) Update Contact")
    print("(5) Delete Contact")
    print("(6) Exit")
    
    option= int(input("Enter an option: "))
    
    if option==1:
      name=input("Enter Name: ")
      phone=int(input("Enter Phone Number: "))
      email=input("Enter E-mail Id: ")
      address=input("Enter Your Address: ")
      Contact[name]={'phone': phone, 
                     'email': email, 
                     'address': address}
  
    elif option==2:
      search_name=input("Enter the Contact Name to Search: ")
      if search_name in Contact:
        details=Contact[search_name]
        print(f"\nDetails for {search_name}:")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
      else:
        print("Name is not found in the Contact book")
    elif option==3:
        View_contact()
      
    elif option==4:
      update_name=input("Enter the contact Name to Update: ")
      if update_name in Contact:
        print("Enter new details :")
        phone=input("New Phone: ") or Contact[update_name]['phone']
        email=input("New Email: ") or Contact[update_name]['email']
        address=input("New Address: ") or Contact[update_name]['address']
        Contact[update_name]={'phone': phone, 
                     'email': email, 
                     'address': address}
        print("Contact Updated Successfully")
      else:
        print("Name is not found in contact book")
        
    elif option==5:
      del_contact=input("Enter the Contact Name to be Deleted: ")
      if del_contact in Contact:
        confirm=input("Do you want to delete this contact? (Yes/No): ")
        if confirm.lower()=='yes':
         del Contact[del_contact]
        else:
          print("deletion Cancelled") 
      else:
        print("Name is not found in contact book")
          
    elif option==6:
      print("Exiting the application")
      break
    else:
      print("Invalid option. Try Again!")
menu()
