"""
I've defined a python class "program" and it contain four different functions
1. swap_two_number : This function swap two variables without using third variable
2. remove_kth_word : This function remove all the occurance of a word after kth occurance
3. palindrom       : If we reverse the number and number comes out to be the same then it is a 
                    palindrom number. This function check weather the number is palindrom or not
4. kth_largest     : This function print's Kth largest number in the array
                      
"""

class program:
    def swap_two_number(self,num1,num2):
        print('original numbers ', num1,num2)
        num1=num1+num2
        num2=num1-num2
        num1=num1-num2
        print('swapped numbers ', num1,num2)
    
    def remove_kth_word(self,string, word,k):
        temp_string = str.lower(str(string))
        temp_word   = str.lower(str(word))
        count=0
        new_string=''
        insert_word=''
        for wd in temp_string.rsplit(' '):
            if wd==temp_word:
                count=count+1
                if count>=k:
                    insert_word=''
                else:
                    insert_word=wd
            else:
                insert_word = wd
            new_string=new_string+insert_word + ' '
        print('old string=', string)
        print('new_string=', new_string)
    
    def palindrom(self,number):
        temp_number = number
        new_number  = 0
        while(True):
            quotient, remainder = divmod(temp_number,10)
            new_number = new_number*10 + remainder
            temp_number = quotient
            if(temp_number == 0):
                break
        if(new_number == number):
            print(number,' is palindrom' )
        else:
            print(number ,' is not palindrom')
    
    def kth_largest(self, arr,k):
        print(arr)
        arr.sort(reverse=True)
        print(arr[k-1])
        

def main():
    pgm =program()
    num1=13
    num2=40
    pgm.swap_two_number(num1,num2)
    string="I'm from India and presently, living in Delhi . Delhi is one of the industrialized city in India"
    word='Delhi'
    pgm.remove_kth_word(string,word,2)
    number=1234321
    pgm.palindrom(number)
    arr=[12,3,41,56,75,34,21,89,76]
    pgm.kth_largest(arr,3)

if __name__ == '__main__':
    main()
