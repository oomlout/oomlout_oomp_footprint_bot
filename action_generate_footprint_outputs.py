import oom_kicad
import os
import oomBase

def go_through_directories():
    oomBase.oomSendAltTab(delay=5)
    count = 1
    count2 = 1
    # go througyh all directories in footprints
    for root, dirs, files in os.walk("footprints"):
        #for each directory
        for name in dirs:
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file

                ######## testing
                #file = "working.kicad_mod"
                if file.endswith(".kicad_mod"):
                    filename = os.path.join(root, name, file)
                    #test
                    #filename = "footprints/alexisvl_ipc7351_least_qfn50p900x900x100_65c/working/working.kicad_mod"
                    #filter = "kicayyyyyC:\GH\oomlout_oomp_footprint_bot\footprints\alexisvl_ipc7351_least_qfn50p800x800x80_49w\working\working.pdf
                    # yd_libraries_kicad"
                    
                    filter = "footprints\\kicad_connector"
                    #filter = "footprints\\kicad_resistor"
                    #filter = "footprints\\kicad_button"
                    #filter = "footprints\\kicad_package"
                    #filter = "footprints\\esden_pkl_led_led_tri_1010"

                    #filter = ""C:\GH\oomlout_oomp_footprint_bot\footprints\alexisvl_ipc7351_least_qfn50p800x800x80_53w4\working\working.pdf
                    
                    # yr = "iangitpers"
                    #if filter in filename.lower():
                    if filename.lower().startswith(filter.lower()):
                        #print("footprint output generating for: " + filename)
                        counter = oom_kicad.generate_outputs_footprint(filename=filename, computer="surface")
                        count += counter
                        #push to git using oom_kicad every 100 files
                        if count % 250 == 0:
                            oom_kicad.push_to_git(count=count)
                            count = count + 1
            count2 = count2 + 1
            if count2 % 100 == 0:
                #print a dot
                print(".", end="", flush=True)
    #oom_kicad.push_to_git(count=count)
                        




if __name__ == '__main__':
    go_through_directories()
    