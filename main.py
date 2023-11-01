
def create_github_repository(username, password, repo_name):
    # Создание нового репозитория
    headers = {'Authorization': 'token YOUR_ACCESS_TOKEN'}
    json_data = {
        "name": repo_name,
        "auto_init": True
    }
    response = requests.post('https://api.github.com/user/repos', json=json_data, headers=headers, auth=(username, password))
    
    if response.status_code == 201:
        print(f"Репозиторий '{repo_name}' успешно создан на GitHub.")
    else:
        print("Не удалось создать репозиторий на GitHub.")
