from collections import Counter

def combine_values(data):
    counter = Counter()
    for d in data:
        item_name = d['item'].replace(" ", "")  # Remove spaces to ensure consistency
        counter[item_name] += d['amount']
    return counter

# Sample data
data = [{'item': 'item 1', 'amount': 400}, 
        {'item': 'item2', 'amount': 300}, 
        {'item': 'item1', 'amount': 750}]

# Example usage
result = combine_values(data)
print(result)  # Output: Counter({'item1': 1150, 'item2': 300})
