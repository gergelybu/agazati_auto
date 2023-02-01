def bevezeto():
    print("I/A:")
    auto = input("\tAutó neve: ")
    gyart_dat = int(input("\tGyártási dátum: "))
    print("I/B:")
    if gyart_dat == 2023:
        print(f"\tEz az {auto} friss gyártás")
    elif gyart_dat < 2000:
        print(f"\tEz az {auto} öreg autó")
    else:
        print(f"\tEz az {auto} átlagos korú")
