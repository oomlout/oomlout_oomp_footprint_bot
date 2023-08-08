import oom_kicad
import os

def go_through_directories():
    count = 1
    # go througyh all directories in footprints
    for root, dirs, files in os.walk("footprints"):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file
                if file.endswith(".kicad_mod"):
                    filename = os.path.join(root, name, file)
                    #filter = "kicad_libraries_kicad"
                    filter = ""
                    # yr = "iangitpers"
                    if filter in filename.lower():
                        counter = oom_kicad.generate_outputs_footprint(filename=filename)
                        count += counter
                        #push to git using oom_kicad every 100 files
                        if count % 250 == 0:
                            oom_kicad.push_to_git(count=count)
                        




if __name__ == '__main__':
    go_through_directories()
    