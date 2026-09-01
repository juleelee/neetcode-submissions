class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_text = re.sub(r'[^a-zA-Z0-9 ]', '', s) 

        str_clean = cleaned_text.split(" ")

        str_clean = "".join(str_clean).lower()

        i = 0 
        j = -1
        while i < len(str_clean)//2:
            
            if str_clean[i] != str_clean[j]:

                print(str_clean[i])
                print(str_clean[j])
                return False

            i +=1
            j-=1
        
            

            




        

        return True


        