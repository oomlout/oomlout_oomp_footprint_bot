import oom_base

directory_old = "C:/GH/oomlout_oomp_footprint_bot2/footprints_old"

def main():
    #go through all files in symbols/
    import os
    count = 1   
    for root, dirs, files in os.walk(directory_old):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file
                if file.endswith("working.yaml"):
                    print(f"Processing {count} {root}")
                    yaml_filename = os.path.join(root, name, file)
                    #load yaml file using yaml
                    import yaml
                    with open(yaml_filename, 'r') as stream:
                        yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
                    #if yaml_dict is an array take element 0
                    if isinstance(yaml_dict, list):
                        yaml_dict = yaml_dict[0]
                    owner = yaml_dict.get("owner","")
                    footprint = yaml_dict.get("footprint","")
                    library = ""
                    library = yaml_dict.get("file","")
                    #split the string at /
                    library = library.split("/")
                    #grab the second to last one
                    library = library[-2]
                    #replace kicad.pretty with ""
                    library = library.replace(".pretty", "")
                    
                    name = yaml_dict.get("name","")
                    name = name.replace(".kicad_mod", "")
                    directory_new = f"{owner}_{library}_{name}"
                    #remove special using oom_base
                    directory_new = oom_base.remove_special_characters(directory_new)
                    directory_new = f"footprints/{directory_new}"
                    pass
                    # image_base_old  is the directory of yaml_filename
                    image_base_old = f"{root}/working"
                    
                    image_base_new = f"{directory_new}/working"

                    images = ["/working.png", "/working_kicad_pcb_3d.png", "/working_kicad_pcb_3d_back.png", "/working_kicad_pcb_3d_front.png"]
                    for image in images:
                        #lower case image
                        image = image.lower()
                        file_image_new = f"{image_base_new}/{image}"
                        #convert \\ to /
                        file_image_new = file_image_new.replace("\\", "/")
                        #remove double //
                        file_image_new = file_image_new.replace("//", "/")
                        file_image_old = f"{image_base_old}/{image}"
                        #convert \\ to /
                        file_image_old = file_image_old.replace("\\", "/")
                        #remove double //
                        file_image_old = file_image_old.replace("//", "/")
                        if os.path.exists(file_image_old):
                            try:
                                if not os.path.exists(file_image_new):
                                    #copy file_image_old to file_image_new
                                    import shutil                                
                                    shutil.copyfile(file_image_old, file_image_new)
                                    print(f"Copying {file_image_old} to {file_image_new}")
                                else:
                                    print(f"Skipping {file_image_old} to {file_image_new} as it already exists")
                            except:
                                print(f"Error copying {file_image_old} to {file_image_new}")



                    
                    
                    
                    
                    
                count += 1
                #print a dot every 1000 files
                if count % 100 == 0:
                    print(".", end="", flush=True)
                    







if __name__ == '__main__':
    main()