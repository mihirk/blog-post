from github import Github

def github_getrepo(repo_name):
    return Github().get_repo(repo_name)

def get_markdown(file):
    return file.name.endswith('.markdown')

def get_post_list(repo):
    file_list = repo.get_dir_contents('/')
    return filter(get_markdown, file_list)

def post_content(post_list):
    return map(lambda x:x.decoded_content, post_list)

def get_posts_from_repo(repo_name):
    repo = github_getrepo(repo_name)
    post_list = get_post_list(repo)
    return post_content(post_list)