def exp(expression):
    left, right = expression.split('=')
    
    def evl_side(side):
        return eval(side.replace('X', '0'))
    
    left_val = evl_side(left)
    right_val = evl_side(right)
    
    x_value = right_val - left_val
    
    if 'X' in left and left[left.index('X') - 1] == '-':
        x_value = -x_value
    
    return x_value

expression = input().strip()
print(exp(expression))
