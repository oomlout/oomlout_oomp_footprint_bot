import tmp.data.oomlout_oomp_footprint_src.oomlout_oomp_footprint_src as oom_f_s
import action_setup
import action_generate_all_footprint_repo
import action_generate_footprint_outputs
import action_generate_readmes
import action_generate_image_resolutions
import action_create_doc
import oom_git


def main(**kwargs):
    repo_filter = "part_template"
    filter = "oomp_footprint_template"
    git = False
    #repo_filter = ""   
    
    kwargs["repo_filter"] = repo_filter
    kwargs["filter"] = filter
    kwargs["git"] = git
    
    
    import time
    time_start = time.time()
    test=False
    dir_src = "tmp/data"
    src_github = "https://github.com/oomlout/oomlout_oomp_footprint_src"
    oom_git.clone(repo = src_github, directory=dir_src)    
    dir_src = f"{dir_src}/oomlout_oomp_footprint_src"
    
    directory = dir_src
    kwargs["directory"] = directory
    kwargs["test"] = test

    #make the repo.yaml file not really needed very often
    if git:
        oom_f_s.make_footprint_yaml(**kwargs)

    #uses repo_filter
    oom_f_s.clone_and_copy_footprints(**kwargs)
   
    oom_f_s.make_footprints_readme(**kwargs)

    #push footprint_src    
    if git:
        oom_git.push_to_git(directory=directory)

    # bot stuff
    action_setup.main()

    action_generate_all_footprint_repo.main()

    ##action_generate_footprint_outputs.main()

    action_generate_readmes.main(**kwargs)

    action_generate_image_resolutions.main(**kwargs)


    action_create_doc.main()

    if git:
        oom_git.push_to_git(comment="comitting after all generations")

    time_end = time.time()
    time_end_hours_and_minutes = time.strftime("%H:%M:%S", time.gmtime(time_end - time_start))
    print(f"Total time: {time_end_hours_and_minutes}")

if __name__ == '__main__':
    main()