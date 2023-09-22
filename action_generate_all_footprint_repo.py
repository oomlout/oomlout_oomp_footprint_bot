import oomlout_oomp_footprint_bot as oom_ofb
import oom_kicad

def main(**kwargs):
    git = kwargs.get("git", True)
    make_library = kwargs.get("make_library", True)
    if make_library:
        oom_ofb.make_temporary_library(**kwargs)
    if git:  
        oom_kicad.push_to_git(repo_directory = "c:/gh/oomlout_oomp_footprint_all_the_kicad_footprints/")






if __name__ == '__main__':
    main()