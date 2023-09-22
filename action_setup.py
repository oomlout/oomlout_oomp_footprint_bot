import oomlout_oomp_footprint_bot as oom_ofb

import oom_kicad



def main(**kwargs):
    git = kwargs.get("git", True)
    oom_ofb.load_data(**kwargs)
    oom_ofb.copy_data(**kwargs)  
    if git:  
        oom_kicad.push_to_git(**kwargs)
    





if __name__ == '__main__':
    main()