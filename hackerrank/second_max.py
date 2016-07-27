no_of_items=int(input())
items=[]
itemsString=input()
# Remove duplicate by making it into a set
# Convert string items to int items and make them a list again
items = set(map(int, itemsString.split()))
# Remove first max item
items.remove(max(items))
# Remove second max item
secondMaxItem=max(items)
print(secondMaxItem)