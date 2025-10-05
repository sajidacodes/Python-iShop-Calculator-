basket_items = []
much_basket = []

print("\n***** Welcome to iShop calculator *****\n")
basket1 = int(input("how many items are there in your basket today?\n"))
if basket1 >0:
 print("let's get to counting them....")
 for basket in range(1,basket1+1):

   name_basket = input(f"Please tell me the name of the item number {basket}\n")
   basket_items.append(name_basket)
   price = float(input(f"What is the price of {name_basket} \n$"))
   much_basket.append(price)
 basket_items2 =input("Would you like to see your entire basket items?(Yes/No)\n").lower()
 if basket_items2 == "yes":
   print("--------")
   for ii in basket_items:
     print(f"-{ii}")
   print("--------")
 else:
  input("Press Enter to exit...")
 much = input("Would you like to see how much it'll cost? (Yes/No)\n").lower()
 if much == "yes":
  print("--------")
  print(f"Buying these items will cost:")
  print(f"${sum(much_basket):.2f}")
  print("--------")
 else:
  input("Press Enter to exit...")
else:
  print("It seems you don't want to buy.")

  
    

    

 



