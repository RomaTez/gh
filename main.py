import requests
def create_github_repo(repo_name):
    username = "RomaTez"
    token = "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"

    headers = {
        "Authorization": f"Token {token}"
    }

    data = {
        "name": repo_name,
        "auto_init": True
    }

    url = f"https://api.github.com/user/repos"

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Репозиторий '{repo_name}' успешно создан!")
    else:
        print(f"Ошибка при создании репозитория: {response.json()['message']}")


repo_name = input("Введите название репозитория: ")
create_github_repo(repo_name)
