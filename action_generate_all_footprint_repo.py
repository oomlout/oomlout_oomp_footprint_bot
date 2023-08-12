import oomlout_oomp_footprint_bot as oom_ofb
import oom_kicad

def main(**kwargs):
    oom_ofb.make_temporary_library()
    oom_kicad.push_to_git(repo_directory = "c:/gh/oomlout_oomp_footprint_all_the_kicad_footprints/")






if __name__ == '__main__':
    main()