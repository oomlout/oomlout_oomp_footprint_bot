import oomlout_oomp_footprint_bot as oom_f_b
import os

def go_through_directories():
    # go through all directories in projects
    for root, dirs, files in os.walk("footprints"):
        #go through all files
        for file in files:
            #check for a brd file
            
            filename = os.path.join(root, file)
            filter = ["sparkfun","adafruit","omerk"]
            filter = ["omerk"]
            filter = [""]
            #filter = ["microsd_yamaichi_pjs_vert"]
            #if any of filter is in filename
            if any(x in filename for x in filter):
                #generate for all with a kicad_pcb file
                if file.endswith(".kicad_mod"):
                    oom_f_b.generate_readme(filename=filename)


if __name__ == '__main__':
    go_through_directories()

