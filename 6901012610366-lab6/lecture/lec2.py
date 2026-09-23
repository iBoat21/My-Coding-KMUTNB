def my_endswith(s, suffix):
    len_s = len(s)
    len_sub = len(suffix)
    
    if len_sub > len_s:
        return False
    
    start_pos = len_s - len_sub
    for i in range(len_sub):
        if s[start_pos + i] != suffix[i]:
            return False
            
    return True

print("--- 2. endswith ---")
print(my_endswith("filename.png", ".png"))  # True
print(my_endswith("hello world", "world"))   # True
print(my_endswith("hello world", "word"))    # False