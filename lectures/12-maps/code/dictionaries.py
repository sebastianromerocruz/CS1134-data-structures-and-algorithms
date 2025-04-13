if __name__ == "__main__":
    # creating
    red_velvet = {}
    print(red_velvet)  # prints {}

    # adding
    red_velvet["Irene"] = "Leader"
    red_velvet["Seulgi"] = "Dancer"
    red_velvet["Wendy"] = "Singer"
    red_velvet["Joy"] = "Dancer"
    red_velvet["Yeri"] = "Rapper"
    print(red_velvet)

    # accessing
    try:
        key = "Wendy"
        wendy = red_velvet[key]
        print(f"{key} exists!")
        
        key = "Taeyeon"
        taeyeon = red_velvet[key]
        print(f"{key} exists!")
    except KeyError:
        print(f"{key} does not exist!")
        
    # removing
    try:
        key = "Wendy"
        del red_velvet[key]
        print(f"{key} removed!")
        
        key = "Taeyeon"
        del red_velvet[key]
        print(f"{key} removed!")
    except KeyError:
        print(f"{key} does not exist!")
        
    # getting size of map
    print(len(red_velvet))
    
    # iterating over keys
    red_velvet["Wendy"] = "Singer"
    
    for member in red_velvet:
        print(f"Member {member}.\tRole: {red_velvet[member]}")
    