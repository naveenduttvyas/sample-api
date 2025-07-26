from git import Repo


def commit_and_push(repo_path, commit_msg, branch="main"):
    repo = Repo(repo_path)
    repo.git.add(A=True)
    repo.index.commit(commit_msg)
    origin = repo.remote(name="origin")
    origin.push(branch)
