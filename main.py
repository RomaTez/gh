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
