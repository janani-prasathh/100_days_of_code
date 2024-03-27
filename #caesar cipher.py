#caesar cipher
letters=['a','b','c','d','e','f','h','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=int(input("type 0 for encode or 1 for decode\n"))
text=input("type your message\n").lower()
shift=int(input("type shift number\n"))
if(shift>26):
    shift%=26
def caesar(plaintext,shiftnumber,direction):
    ciphertext=""
    for letter in plaintext:
        position=letters.index(letter)
        if(direction==0):
            newposition=position+shiftnumber
            
        else:
            newposition=position-shiftnumber
        new_letter=letters[newposition]
        ciphertext+=new_letter
    if(direction==0):
        print(f"the encrypted word is {ciphertext}")
    else:
        print(f"the decrypted word is {ciphertext}")

caesar(text,shift,direction)
