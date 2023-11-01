import requests

def create_github_repository(repo_name):
    # Создание нового репозитория
    headers = {'Authorization': 'token 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'}
    json_data = {
        "name": repo_name,
        "auto_init": True
    }
    response = requests.post('https://api.github.com/user/repos', json=json_data, headers=headers, auth=("RomaTez", "04izaholSS!"))
    
    if response.status_code == 201:
        print(f"Репозиторий '{repo_name}' успешно создан на GitHub.")
    else:
        print("Не удалось создать репозиторий на GitHub.")
name = input("Repository name")
create_github_repository(name)
