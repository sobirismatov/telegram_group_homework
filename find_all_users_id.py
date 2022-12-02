from read_data import read_data
data=read_data("data/result.json")
def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    dic=data["messages"]
    a=[]
    for i in dic:
        if i["type"]=="service":
            if i['actor_id'] not in a:
                a.append(i["actor_id"])
        elif i["type"]=="message" :
            if i["from_id"] not in a:
                a.append(i["from_id"])
    return a
print(find_all_users_id(data))