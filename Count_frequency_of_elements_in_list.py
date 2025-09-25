def count_freq(nums):
    count_dict=dict()
    for num in nums:
        if(num in count_dict):
            count_dict[num]=count_dict[num]+1
        else:count_dict[num]=1
    print(count_dict)
if __name__ =="__main__":
    count_freq([1,1,1,2,3,1,2])