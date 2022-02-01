
# define a function that searches a given file for a given keyword
# and return the line and index of keyword in the text
def file_search(file_name, keyword):
    # open file and set it to a variable
    file = (open(file_name)).read()
    # the keyword is in the text
    if keyword in file:
        # split the text into a list of lines
        lines = file.splitlines()
        # find the line the keyword is on
        for l in lines:
            if keyword in l:
                line_index = lines.index(l)
                # split the line into words
                words = lines[line_index].split()
                # find the index of the word in the line
                for w in words:
                    if keyword in w:
                        word_index = words.index(w)
                        break
                    else:
                        continue
                break
            else:
                continue
        # return the line and index
        return (f"The word is on line {line_index + 1} at index {word_index + 1}")
    # the keyword is not in the file
    else:
        return ("The file does not contain that word.")
    
