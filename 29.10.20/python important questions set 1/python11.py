#P E MD AS Rule 

def generate_ngrams(text,n):
    words=text.split()
    output=[]
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    print(output)


generate_ngrams("This is a sample text",3)

