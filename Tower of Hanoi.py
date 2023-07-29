#July 30, 01:23am

def Hanoi(n, source, intermediate, destination):
    if not n:
        return 0
    
    Hanoi(n-1, source, destination, intermediate)
    print(f'Moved donut {n} from {source} to {destination}')
    Hanoi(n-1, intermediate, source, destination)

    return 0

size = int(input("Enter the size of Hanoi Tower:"))

print("\nStarting Operation!\n")
Hanoi(size, "A", "B", "C")
print("\nOperation Complete!")