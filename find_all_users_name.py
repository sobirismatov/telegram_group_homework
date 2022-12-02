from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    data=data["messages"]
    a=[]
    for i in data:
        if i["type"]=="service" :
            if i["actor_id"] not in a:
               a.append(i["actor"])
        elif i["type"]=="message" :
            if i["from_id"] not in a:
               a.append(i["from"])
    return a
data=read_data("data/result.json")
print(find_all_users_name(data))