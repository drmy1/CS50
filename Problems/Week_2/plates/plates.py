def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = str(s)
    
    
    last = []
    alnum = []
    for i in range(len(s)):
        last.append(s[i])        
    
    if s.isalnum() == True:       
        if len(s) <= 6:
                for k in range(len(s)):
                    placeholder = str(s[k])
                    if placeholder.isalpha():
                        alnum.append(1)
                        if k == 0:
                            pass                        
                        else: 
                            if ((alnum[k] == 1) & (alnum[k-1] == 1)):
                                if k == len(s)-1:
                                    return True
                                else:
                                    pass
                            elif ((alnum[k-1] == 1) & (alnum[k] == 0)):
                                if k == len(s)-1:
                                    return True
                                else:
                                    pass
                            else:
                                return False
                            
                    else:
                        alnum.append(0) 
                        if k == 0:
                            pass
                        else:
                            if ((alnum[k-1] == 0) & (alnum[k] == 0)):
                                if k == len(s)-1:
                                    return True
                                else:
                                    pass
                            elif ((alnum[k-1] == 1) & (alnum[k] == 0)):
                                if k == len(s)-1:
                                    return True
                                else:
                                    pass    
                            else:

                                return False
                                
                            
                    
                           
        else:
            return False
                      
    else:
        return False
        
        

if __name__ == "__main__":

    main()