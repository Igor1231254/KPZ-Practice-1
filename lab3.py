def palindrom(text):
    words = text.split()
    palindromes = []  

    for word in words:
        
        if word == word[::-1]:  
            palindromes.append(word) 

    return palindromes 
  
  ######################################
  
  def validate_ip(ip_address):
    
    octets = ip_address.split(".")
    
   
    if len(octets) != 4:
        return False
    
    
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
    
    return True  

  
  ##########################################################################
  
  import platform

def get_os():

    system = platform.system()
    
    if system == "Darwin":
        return "Mac"
    elif system == "Windows":
        return "Windows"
    elif system == "Linux":
        return "Linux"
    else:
        return None
