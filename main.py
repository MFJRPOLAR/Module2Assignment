from serialsearch import * 

def main():
    #First Prompt
    list1 = ['E','B','E','F','A','F'] 
    list2 = ['E','B','E','F','A','F']

    # Second Prompt 
    #list1 = ['E','B','E','F','A','C'] 
    #list2 = ['E','B','E','F','A','F'] 

    #Third Prompt 
    #list1 = ['E','B','E','F','A','F','C'] 
    #list2 = ['E','B','E','F','A','F']
    
    list3 = []
  
    i = 0 
    if len(list1) != len(list2):
        notsame(list1,list2)
        exit()

    while (i < len(list1)):   
        if search(list1, i, len(list1), list2[i]) != -1: 
           list3.append(list1[i]) 
        else:
            notsame(list1,list2)
            break
        i += 1

    if list3 == list1 and list3 == list1:
        print("Two lists are strictly identical!")
        print(f"List 1: {list1}")
        print(f"List 2: {list2}")
    else: 
        exit()

def notsame(list1,list2):
    print("Two lists aren't strictly identical!")
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")

if __name__ == "__main__":
    main()