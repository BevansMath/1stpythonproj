



file = ''      # input wordlist or text file
file2 = ''     #Output file is a sorted text file parsed for keyword frequencies
with open(file, encoding='utf8') as f:
    with open('', 'w') as output:
         word = input("Enter a word: ") #User inputs a word or phrase
         status = int(input("Enter a status code:"))
         num_line = 1 # Initialize variable line at line 1
         for line in f:
             if word in line: # If word is in the line, ...
                print("line {}: {}".format(num_line, line.strip()))
                output.writelines(line) # Line gets placed in output file
         line = f.readline()
         num_line += 1

    print("Here are websites with keyword" + word)