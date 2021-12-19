# Dial *211#
dial = eval(input("Dial *211#"))

# if dial.length() != 5:
# The main menu
print("1.Buy Airtime/Bundle\n2.Send Money\n3.Make payment\n4.Withdraw Money\n5.Kutchova\n6.Bank\n7.My Account\n8.Change language")

# Selecting the main menu
menu = eval(input("Please select: "))

if menu < 1 or menu > 8:
    print("Invalid Input.Try again later")
    sys.exit(menu)

if menu == 1:
    print("1.Buy Airtime\n2.Buy Bundle")

elif menu == 2:
    print("1.Airtel number\n2.TNM number\n3.Other Accounts")

elif menu == 3:
    print("1.Make Payments\n2.Buy Goods and Services\n3.Retailer Stock Purchase")

elif menu == 4:
        agent_code = eval(input("Enter Agent code: "))

elif menu == 5:
    print("1.Kutchova\n2.Kutchova Loan")

elif menu == 6:
    print("ECO Bank\n2.FDH Bank\n3.FCB\n4.NSB\n5.Standard Bank\n6.National Bank\n7.My Backs\n8.Finca")

elif menu == 7:
    # my account
    print("1.My PIN\n2.Change Nickname\n3.Reports\n4.Merchant On Boarding\n5.Check Balance\n6.My Favorites\n7.My Transaction Reversals")

else:
    print("1.Chichewa\n2.English")

    language_select = eval(input("Please select language: "))

    while language_select < 1 or language_select > 2:
        language_select = eval(input("Invalid Input.Please select again: "))
        if language_select == 1:
            print("Chichewa selected")
        elif language_select == 2:
            print("English selected")  
