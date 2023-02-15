import requests
from bs4 import BeautifulSoup as BS

def get_profile_img(github_user: str):
    url = f"https://github.com/{github_user}"
    response = requests.get(url)
    get_content = BS(response.content, "html.parser")
    
    profile_img_element = get_content.find('img',{'alt' : 'Avatar'})
    profile_img = profile_img_element['src']

    test_dict = {
        "edno": 1,
        "dve": 2,
        "tri": 3
    }

    print(test_dict)
    
    test_tuple = ("uno", "duos")

    # test_tuple[1] = "tres"  # DO NOT DO, TUPLES CANNOT BE ALTERED
    print(f"{test_tuple[1]=}")
    print(f"{type(test_tuple)=}\n{test_tuple=}")

    # dictionary    - unordered list of non-unique named values, with unique keys! , access via key
    # list          - non-unique values, ordered list, access via index
    # set           - unique values, ordered list, access via index
    # tuple         - non-unique values, ordered list, access via index, NON ALTERABLE/CHANGABLE

    for key, value in enumerate(test_dict.items()):
        print(f"{key} -> {value}")

    # print(f"{get_content=}")

    # profile_img = profile_img['src']
    # why src is outside ? and how find works img then alt and avatar
    
    return profile_img


def main():
    # github_usr = input("Please type an existing Github user account: ")
    github_usr = "NAtanassov"
    print(f"{get_profile_img(github_user = github_usr)=}")


if __name__ == "__main__":
    main()


#how to get number of repos