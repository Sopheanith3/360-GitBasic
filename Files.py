def main():
    # Ask user for file name and opens file
    user_input = (str(input('Type the file you want open(Include file extension name): ')))
    user_file = open(user_input, 'r') # Enter otherData.txt or data.txt
    even_file = open('even.txt', 'w')
    odd_file = open('odd.txt', 'w')
    
    print('Opening', user_input, 'file')
    
    # Initialize even sum
    even_sum = 0
    negative_count = 0
    # Reads the file
    for line in user_file:
        num = int(line)

        # Checks if the file numbers are even or odd
        if (num % 2) == 0:
            even_file.write(str(num) + '\n')
            even_sum += num
        else:
            odd_file.write(str(num) + '\n')
            
        # Counts how many negative numbers in file
        if num < 0:
            negative_count += 1
            
    user_file.close()
    even_file.close()
    odd_file.close()

    ## Outputs
    print('The sum of all even numbers in your file are:',even_sum)
    print('There are',negative_count,'odd numbers in your file')
    
main()
