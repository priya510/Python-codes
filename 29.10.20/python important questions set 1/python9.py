values=[1,2,3,4]        #[1,2,3,4]
numbers=set(values)     #{1,2,3,4}

def checknums(num):
    if num in numbers:
        return True
    else:
        return False

for i in filter(checknums,values):
    print(i)

