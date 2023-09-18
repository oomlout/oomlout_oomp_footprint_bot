import tmp.data.oomlout_oomp_footprint_src.oomlout_oomp_footprint_src as oom_f_s
import action_setup
import action_generate_all_footprint_repo
import action_generate_footprint_outputs
import action_generate_readmes
import action_generate_image_resolutions
import action_create_doc
import oom_git


def main(**kwargs):
    import time
    #time_start 
    test=False
    dir_src = "tmp/data/"
    src_github = "https://github.com/oomlout/oomlout_oomp_footprint_src"
    oom_git.clone(repo = src_github, directory=dir_src)    
    dir_src = f"{dir_src}/oomlout_oomp_footprint_src"
    
    directory = dir_src

    #make the repo.yaml file not really needed very often
    #oom_f_s.make_footprint_yaml(directory=directory, test=test)

    #oom_f_s.clone_and_copy_footprints(directory=directory, test=test)
   
    ##oom_f_s.make_footprints_readme()

    #push footprint_src    
    #oom_git.push_to_git(directory=directory)

    # bot stuff
    #action_setup.main()

    #action_generate_all_footprint_repo.main()

    ##action_generate_footprint_outputs.main()

    #action_generate_readmes.main()

    action_generate_image_resolutions.main()


    action_create_doc.main()

    oom_git.push_to_git(comment="comitting after all generations")



    #oomlout_oomp_symbol_src.clone_and_copy_symbols(test=test, dir_base="tmp/data/oomlout_oomp_symbol_src")
    #oomlout_oomp_symbol_src.make_symbols_readme()
    #dir_all_symbols = "tmp/data/oomlout_oomp_symbol_all_the_kicad_symbols"
    #oom_git.push_to_git(directory=dir_all_symbols)
    #action_setup.main()
    #action_generate_symbol_outputs.main()
    #action_generate_readmes.main()
    #action_generate_image_resolutions.main()


if __name__ == '__main__':
    main()