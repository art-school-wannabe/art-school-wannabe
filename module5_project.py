
def file_search(file_name, keyword):
    file = (open(file_name)).read()
    if keyword in file:
        index = file.index(keyword)
        return (f"The word is at index {index}.")
    else:
        return ("The file does not contain that word.")
