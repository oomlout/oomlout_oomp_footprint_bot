import oom_base
import oom_git



def main(**kwargs):
    #go through all files in symbols/
    filter = kwargs.get("filter", [""])
    git = kwargs.get("git", True)
    #if filter isn't an array make it one
    if not isinstance(filter, list):
        filter = [filter]
    import os
    oom_base.image_resolutions_dir(directory="footprints", filter=filter, git=git, git_per = 20000)
    
    if git:
        oom_git.push_to_git(count=100 )






if __name__ == '__main__':
    main()