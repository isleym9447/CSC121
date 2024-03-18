# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def print_dict(contacts):


    print(f'{"Name":<10}{"Phone":<10}')
    print("-"*22)
    
    for k, v in contacts.items():
     
    
    
        print(f'{k:<10}{v:<10}')
    
def write_dict(contacts):
    
    #approach one (three steps we no like)
    
    #create a file object that refrences the file
    
    outfile = open('contacts.txt', 'w')
    
    #step 2
    
    outfile.write(f'{"Name":<10}{"Phone":<10}\n')
    outfile.write("-"*22+"\n")

   
    
    for k, v in contacts.items():
     
    
    
        outfile.write(f'{k:<10}{v:<10}\n')
        
        #step 3 close
        
    outfile.close
    
    
    
#approach 2 we like
    
    #step 1 opens and closes at end
    
    with open('contacts.txt','w') as outfile:
    
        #step 2
        
        outfile.write(f'{"Name":<10}{"Phone":<10}\n')
        outfile.write("-"*22+"\n")
    
       
        
        for k, v in contacts.items():
         
        
        
            outfile.write(f'{k:<10}{v:<10}\n')
    
    
    
#approach 3 we also like but slightly less ONLY TEXT FILES!!!

    #step 1 
    
    with open('contacts.txt','w') as outfile:
    
        #step 2
        
        print(f'{"Name":<10}{"Phone":<10}', file=outfile)
        print("-"*22+"\n", file=outfile)
    
       
        
        for k, v in contacts.items():
         
        
        
            print(f'{k:<10}{v:<10}\n', file=outfile)
    
    
    
    
    
    
def main():
    
    contacts = {"Jon":"910-698-7896", "Susan":"910-123-4567", "Sam":"910-567-8910"}
    
    print_dict(contacts)
    
    write_dict(contacts)
    
    #print_write_dict(contacts)
    
    
    
    
    if __name__=="__main__":
        
        main()
    
    























