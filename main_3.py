
# def my_function():
#     return "This is the result from my_function @@2!! "
# result = my_function()

# file_path = r'D:\Projects\kivy project\service_name.txt'
# with open(file_path, 'r') as file:
#     existing_content = file.read()

# updated_content = result + '\n' + existing_content

# with open(file_path, 'w') as file:
#     file.write(updated_content)

# print(result)

#   github_token = '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'
#  https://github.com/manishprajapat01997/kivy_project/tree/main






# upload .py file (github)

import requests
import base64

def upload_to_github(username, repository, file_path, branch, token):
    # Read the content of the file in binary mode
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Encode the binary content in Base64
    encoded_content = base64.b64encode(file_content).decode()

    # GitHub API endpoint to create or update a file
    url = f'https://api.github.com/repos/{username}/{repository}/contents/{file_path}'

    # Check if the file already exists
    response = requests.get(url, headers={'Authorization': f'Token {token}'})
    
    if response.status_code == 200:
        # File exists, generate a new file name with a numeric suffix
        base_name, extension = file_path.split('.')
        i = 1
        while True:
            new_file_path = f'{base_name}_{i}.{extension}'
            url = f'https://api.github.com/repos/{username}/{repository}/contents/{new_file_path}'
            response = requests.get(url, headers={'Authorization': f'Token {token}'})
            if response.status_code != 200:
                break
            i += 1
        file_path = new_file_path

    # Set up the headers and payload
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }

    payload = {
        'message': f'Upload {file_path}',
        'content': encoded_content,
        'branch': branch
    }

    # Make the request to GitHub API
    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f'Successfully uploaded {file_path} to GitHub.')
    else:
        print(f'Failed to upload {file_path} to GitHub. Status code: {response.status_code}, Response: {response.text}')


def main():
    github_username = 'manishprajapat01997'
    github_repository = 'kivy_project'
    # file_to_upload = 'D:/Projects/kivy project/new file/app1.py'

    file_to_upload = 'main.py'
    # file_to_upload = 'install_service.py'
    github_branch = 'main'
    github_token = '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'

    upload_to_github(github_username, github_repository, file_to_upload, github_branch, github_token)


if __name__ == "__main__":
    main()










