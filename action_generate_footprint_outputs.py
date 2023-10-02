import oom_kicad
import os
import oomBase

def go_through_directories(**kwargs):
    filter = kwargs.get("filter", "")
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
                    if not isinstance(filter, list):
                        filter = [filter]
                                    
                    if any(x in filename for x in filter):                    
                        #print("footprint output generating for: " + filename)
                        counter = oom_kicad.generate_outputs_footprint(filename=filename, computer="surface")
                        count += counter
                        #push to git using oom_kicad every 100 files
                        if count % 250 == 0:
                            import action_generate_image_resolutions
                            action_generate_image_resolutions.main()
                            #push now in
                            #oom_kicad.push_to_git(count=count)
                            count = count + 1
            count2 = count2 + 1
            if count2 % 100 == 0:
                #print a dot
                print(".", end="", flush=True)
    import action_generate_image_resolutions
    action_generate_image_resolutions.main()
                        





if __name__ == '__main__':
    kwargs = {}
    #kwargs["filter"] = ["oomlout"]
    kwargs["filter"] = [""]
    go_through_directories(**kwargs)
    