#Prompt the user to enter string
word = input("Enter the word ")

#set index_start to zero
index_start = 0

#set index_end to last character
index_end = len(word)-1

#compare the characters from start to end, index_start < index_end
while index_start < index_end:

# if equal, update the start & end index
    if word[index_start] == word[index_end]:
        index_start = index_start + 1
        index_end =  index_end - 1
# else stop checking
    else:
        break
#Verify result
if index_start < index_end:
    print("Non Pallindrome")
else:
    print("Pallindrome")    