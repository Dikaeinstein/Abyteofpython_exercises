import cwd
import string

def reverse(text):    
    return text[::-1]
    
def is_palindrome(text): 
    res = []    
    text_list = text.lower().split(" ")
    for i in text_list:
        i = i.strip(string.punctuation)
        #print(i)
        res.append(i)
    
    return "".join(res) == reverse("".join(res))
    
something = input('Enter text: ')

if (is_palindrome(something)):    
    print("Yes, it is a palindrome")
else:    
    print("No, it is not a palindrome")
    
    
poem = """\
Programming is fun
when the work is done
if you wanna make your work also fun:
    use python!
"""    
with open("poem.txt", "w") as f:
    f.write(poem)    
    
with open("poem.txt") as f:
    for line in f:
        print(line, end="")