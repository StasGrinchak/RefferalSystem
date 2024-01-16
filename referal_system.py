from datetime import datetime


users_data = {
    "user1": {
        "id": 1,
        "date_joined": "01/10/2024",
        "invited_users": ["user2", "user3"],
        "purchasing_package": "Package 2",
        "package_purchase_date": "01/11/2024",
        "buster_bonus": 0
    },
    "user2": {
        "id": 2,
        "date_joined": "01/12/2024",
        "invited_users": ["user4"],
        "purchasing_package": "Package 2",
        "package_purchase_date": "01/12/2024",
        "buster_bonus": 0
    },
    "user3": {
        "id": 3,
        "date_joined": "01/13/2024",
        "invited_users": [],
        "purchasing_package": "Package 3",
        "package_purchase_date": "02/13/2024",
        "buster_bonus": 0
    },
    "user4": {
        "id": 4,
        "date_joined": "01/15/2024",
        "invited_users": [],
        "purchasing_package": "Package 2",
        "package_purchase_date": "01/15/2024",
        "buster_bonus": 0
    },
    "user5": {
        "id": 5,
        "date_joined": "01/16/2024",
        "invited_users": [],
        "purchasing_package": "Package 3",
        "package_purchase_date": "01/16/2024",
        "buster_bonus": 0
    },
}


def get_all_refferel_users(invited_users: list) -> set:
    """
    Function for getting all referral users (the first 2 invited and their next 2). 
    Returns: 
        set : referral user names.
    """
    users_name_set = set(invited_users)
    for name in invited_users:
        child_refferal_users = users_data[name]["invited_users"]
        users_name_set = set(child_refferal_users) | users_name_set
    return users_name_set


def checking_registration_by_time(package_purchase_date: str, invited_user_registration: str) -> bool:
    """
    Checking the referral user on the date of registration, 
    which must be within a month from the date of registration of the initial user.

    Returns: 
        True : if a person enters the time range,
        False: if the person not enters the time range.
    """
    user_registration_date = datetime.strptime(package_purchase_date, "%m/%d/%Y")
    invited_user_registration_date = datetime.strptime(invited_user_registration, "%m/%d/%Y")
    if (invited_user_registration_date - user_registration_date).days > 30:
        return False
    return True


def referral_system(users_data: dict) -> None:
    """
    Function for accruing Booster bonuses to the user using the so-called referral link.
    """
    for user_name, user_data in users_data.items():
        invited_users = user_data.get('invited_users')
        purchasing_package_user = user_data.get('purchasing_package')
        package_purchase_date = user_data.get('package_purchase_date')

        if len(invited_users) >= 2 and purchasing_package_user in ["Package 2", "Package 3"]:
            all_users_name = get_all_refferel_users(invited_users=invited_users)
            
            suitable_users = list()
            for reff_user_name in all_users_name:
                invited_user_data = users_data[reff_user_name]
                invited_user_registration = invited_user_data.get('date_joined')
                if checking_registration_by_time(package_purchase_date, invited_user_registration):
                    purchasing_package = invited_user_data.get('purchasing_package')
                    if purchasing_package in ["Package 2", "Package 3"]:
                        suitable_users.append(reff_user_name)
            if len(suitable_users) >= 6:
                count_booster_bonus = len(suitable_users) // 6
                user_data['buster_bonus'] = user_data['buster_bonus'] + count_booster_bonus
                print(f'{user_name} received {count_booster_bonus} bonuses thanks to these users - {suitable_users}')
            suitable_users.clear()
    print(users_data)
                        
                
if __name__ == "__main__":
    referral_system(users_data=users_data)