def obfuscate(email):
        
        if "@" or "dot" in email:
            ab = email.replace("@", " [at] ").replace(".", " [dot] ")    
        return ab


email = "33.test@123.com"
print(obfuscate(email))