import oomlout_oomp_footprint_bot as oom_ofb

import oom_kicad



def main():
    oom_ofb.load_data()
    oom_ofb.copy_datxa()    
    oom_kicad.push_to_git()
    





if __name__ == '__main__':
    main()