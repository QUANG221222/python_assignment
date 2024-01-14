""" character=input("Enter a single character: ")
if((character>'a' and character<'z') or (character>'A' and character<'Z') ):
    character=character.lower()
    if (character=='u' or character=='e' or character=='o' or character=='a' or character=='i' ):
        print(f"The character '{character}' is a vowel")
    else: print(f"The character '{character}' is a consonant")
else: print("Errol !!!") """
""" list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
l=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            l.append(list1[i])
print("Common element: ",l) """
def is_palindrome(input_str):
    input_str=str(input_str)
    input_str=input_str.lower().replace(" ","")
    return input_str==input_str[::-1]
input_str=input("Enter a word or phrase: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome")
else: print(f"'{input_str}' is not a palindrome")