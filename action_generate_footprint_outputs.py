import oom_kicad
import os

def go_through_directories():
    count = 1
    count2 = 1
    # go througyh all directories in footprints
    for root, dirs, files in os.walk("footprints"):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file
                if file.endswith(".kicad_mod"):
                    filename = os.path.join(root, name, file)
                    #filter = "kicayyyyyC:\GH\oomlout_oomp_footprint_bot\footprints\alexisvl_ipc7351_least_qfn50p800x800x80_49w\working\working.pdf
                    # yd_libraries_kicad"
                    filter = ""
                    #filter = ""C:\GH\oomlout_oomp_footprint_bot\footprints\alexisvl_ipc7351_least_qfn50p800x800x80_53w4\working\working.pdf
                    
                    # yr = "iangitpers"
                    if filter in filename.lower():
                        print("footprint output generating for: " + filename)
                        counter = oom_kicad.generate_outputs_footprint(filename=filename)
                        count += counter
                        #push to git using oom_kicad every 100 files
                        if count % 250 == 0:
                            oom_kicad.push_to_git(count=count)
                            count = count + 1
            count2 = count2 + 1
            if count % 5000 == 0:
                #print a dot
                print(".", end="", flush=True)
    oom_kicad.push_to_git(count=count)
                        




if __name__ == '__main__':
    go_through_directories()
    