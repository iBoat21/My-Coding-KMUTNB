def my_isalpha(s):
    if len(s) == 0:
        return False
    
    for i in range(len(s)):
        code = ord(s[i])
        is_upper = (65 <= code <= 90)
        is_lower = (97 <= code <= 122)
        
        if not (is_upper or is_lower):
            return False
            
    return True

print("--- 3. isalpha ---")
print(my_isalpha("HelloWorld"))  # True
print(my_isalpha("Hello123"))    # False 
print(my_isalpha("Hello World"))  # False