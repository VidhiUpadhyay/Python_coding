def merge(dict1,dict2):
    "Method 1"
    merged_dict={**dict1,**dict2}
    print(merged_dict)
    "Method 2"
    for key,value in dict2.items():
        dict1[key]=value
    print(dict1)

if __name__=="__main__":
    dict1={"name":"John", "age":10,"grade":3}
    dict2={"hobby":"painting","city":"London"}
    merge(dict1,dict2)