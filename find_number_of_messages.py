from read_data import read_data
data=read_data("data/result.json")
def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    dic=data["messages"]
    a=[]
    for i in dic:
        if i["type"]=="message":
            a.append(i["id"])
    return len(a)
print(find_number_of_messages(data))
