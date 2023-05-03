def greet(name):
    print (f"hi {name}")
    return"..."
    
print (greet ("Mosh"))
    
def get_greeting (name):
    return f"Hi {name}"

message = get_greeting ("Mosh")
file = open ("content.txt", "w")
file.write(message)
