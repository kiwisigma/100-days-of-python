# function with return



def enough_money(inserted, cost):
    if inserted < cost:
        print(f"Now enough!")
        return False
    else:
        return True