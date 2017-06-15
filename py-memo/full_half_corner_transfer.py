def ToHalf(ustring):    
    rstring = ""  
    for uchar in ustring:  
        inside_code=ord(uchar)  
        if inside_code == 12288: # space           
            inside_code = 32  
        elif (inside_code >= 65281 and inside_code <= 65374): 
		# except space 
            inside_code -= 65248  
            rstring += chr(inside_code)  
    return rstring
def ToFull(ustring):    
    rstring = ""  
    for uchar in ustring:  
        inside_code=ord(uchar)  
        if inside_code == 32: # space         
            inside_code = 12288
        elif (inside_code >= 65281-65248 and inside_code <= 65374-65248): 
		# except space 
            inside_code += 65248  
            rstring += chr(inside_code)  
    return rstring