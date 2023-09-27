import tmp.data.oomlout_oomp_footprint_src.oomlout_oomp_footprint_src as oom_f_s
import action_setup
import action_generate_all_footprint_repo
import action_generate_footprint_outputs
import action_generate_readmes
import action_generate_image_resolutions
import action_create_doc
import oom_git

 # test oomlout_oomlout_oomp_footprint_templates_oobb_connector_basic_triple
def main(**kwargs):
    
    
    #### run settings
    repo_filter = "oomlout"
    #repo_filter = ""
    
    filter = "oomlout"
    #filter = ""
    
    #git = False
    git = True
      
    test=False
    #test=True

    overwrite = False       #whetether to do all or just the missing ones
    #overwrite = True
      
    

    ###### load into kwargs
    directory = "tmp/data/oomlout_oomp_footprint_src"
    all = False#if repo and repofilter both equal [""] then all is true
    if repo_filter == [""] and filter == [""]:
        print("repo_filter and filter both equal [''] so all is true")
        all = True
    kwargs["all"] = all
    #if repo_filter isn't a list make it one
    if type(repo_filter) != list:
        repo_filter = [repo_filter]
    kwargs["repo_filter"] = repo_filter
    #if filter isn't a list make it one
    if type(filter) != list:
        filter = [filter]
    kwargs["filter"] = filter
    kwargs["git"] = git
    kwargs["directory"] = directory
    kwargs["test"] = test
    kwargs["overwrite"] = overwrite
    
    
    import time
    time_start = time.time()
    
    src_github = "https://github.com/oomlout/oomlout_oomp_footprint_src"
    oom_git.clone(repo = src_github, directory="tmp/data")    
    
    
    
    #make the repo.yaml file not really needed very often
    if git:
        print
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Making repo.yaml file pulling libraries from mega library repo")
        oom_f_s.make_footprint_yaml(**kwargs)

    #uses repo_filter
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Copying data to footprints directory")
    oom_f_s.clone_and_copy_footprints(**kwargs)
    
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Making  src readme.md files")
    oom_f_s.make_footprints_readme(**kwargs)

    #push footprint_src    
    if git:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Pushing to git")
        oom_git.push_to_git(directory=directory)

    # bot stuff
    print("bot stuff")
    action_setup.main(**kwargs)

    
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> making the all footprints repo")
    action_generate_all_footprint_repo.main(**kwargs)

    ##action_generate_footprint_outputs.main()

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> generating bot readmes")
    action_generate_readmes.main(**kwargs)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> generating image resolutions")
    action_generate_image_resolutions.main(**kwargs)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> creating doc")
    action_create_doc.main(**kwargs)

    if git:
        oom_git.push_to_git(comment="comitting after all generations")

    time_end = time.time()
    time_end_hours_and_minutes = time.strftime("%H:%M:%S", time.gmtime(time_end - time_start))
    print(f"Total time: {time_end_hours_and_minutes}")

if __name__ == '__main__':
    main()