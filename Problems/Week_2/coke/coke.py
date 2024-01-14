def main():
    
    print("Amount Due: 50")
    left = 50
    insert(left) 
    

def insert(left):
    coin = int(input("Insert Coin: "))
    
    match coin:
        case 25 | 10 | 5:
            left = amount_due(coin, left)
            if left <= 0:
                print(f"Change Owed: {abs(left)}")
            else:
                print(f"Amount Due: {left}")
                insert(left)
        case _:
            print(f"Amount Due: {left}")
            insert(left)
            
            
def amount_due(coin, left):
    priceleft = left - coin
    return priceleft
    

if __name__ == "__main__":
    main()