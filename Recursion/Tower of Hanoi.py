#July 30, 01:23am

def Hanoi(n, source, intermediate, destination):
    if not n:
        #return if there are no more donuts to move
        return 0
    
    Hanoi(n-1, source, destination, intermediate)               #move donuts above current donut to intermediate tower
    print(f'Moved donut {n} from {source} to {destination}')    #move current donut to destination
    Hanoi(n-1, intermediate, source, destination)               #move remaining donuts from intermediate to destination

    return 0

size = int(input("Enter the size of Hanoi Tower:"))

print("\nStarting Operation!\n")
Hanoi(size, "A", "B", "C")
print("\nOperation Complete!")