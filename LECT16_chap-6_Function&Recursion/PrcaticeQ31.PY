# WAF to print elements of a list in a single line.(list is the parameter)
cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes=["thor","ironmen","shaktiman"]
# print(cities[2], end=" ")
# print(heroes[1])


def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)        
print_list(cities)
print()   