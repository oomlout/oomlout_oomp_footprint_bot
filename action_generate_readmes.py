import oomlout_oomp_footprint_bot as oom_f_b
import os
import oom_kicad


def main():
    go_through_directories()

def go_through_directories():
    count = 1
    count2 = 1
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
                    count = count + 1
                    print(f"{count}  ", end="", flush=True)
        
        #push every 5000
        if count % 20000 == 0:
            oom_kicad.push_to_git(count=count)
            count = count + 1
        
    oom_kicad.push_to_git(count=count)


if __name__ == '__main__':
    go_through_directories()

