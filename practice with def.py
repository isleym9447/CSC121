
def main():

    start, end = get_nums()
    
    display_list(s,end)
    

def display_list(start, end):

    print(f'["number":<10] ["square":<10]["cube":<10]')
    for x in range(start,end+1): #for loop going from 0 to 5
            print(f'{x:<10}{x ** 2:<10}{x ** 3:<10}')

# function asks user to enter start and end numbers and returns them


def get_nums():

    #get s and end
    
    s = int(input("Enter starting num: "))

    end = int(input("Enter ending num: "))

    return s, end

    
main()
