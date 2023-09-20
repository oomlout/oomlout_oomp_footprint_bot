import os
import shutil
import oom_base

def main():
    overwrite = True
    directory_doc = "c:/gh/oomlout_oomp_footprint_doc"
    #if directory doesn't exist, create it
    if not os.path.exists(directory_doc):
        os.makedirs(directory_doc)
    #recursively go through all files in the symbols directory
    count = 1
    for root, dirs, files in os.walk("footprints"):
        #for every file
        for file in files:
            if "working.yaml" in file:
                directory = root.replace("\\", "/")

                src = os.path.join(root, file)
                src = src.replace("\\", "/")

                yaml_file = f'{directory}/{file}'
                yaml_file = yaml_file.replace("\\", "/")
                #load yaml file
                import yaml
                with open(yaml_file) as f:
                    yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
                #if yaml_dict is a list take element 0
                if isinstance(yaml_dict, list):
                    yaml_dict = yaml_dict[0]
                
                
                owner = yaml_dict.get("owner", "")
                owner = owner.lower()

                footprint = yaml_dict.get("footprint", "")
                footprint_name = ""
                if footprint != "":
                    footprint_name = str(footprint.get("libraryLink", ""))
                    footprint_name = footprint_name.lower()
                    #remove special characters
                    footprint_name = oom_base.remove_special_characters(footprint_name)
                    library = yaml_dict.get("oomp_key", "")
                    library = library.replace(f"oomp_{owner}_", "")
                    library = library.replace(f"_{footprint_name}", "")
                    last_library = library

                else: # if no footprint to get foorprint name   from, use the last library
                    library = last_library

                    footprint_name = yaml_dict.get("oomp_key", "")
                    footprint_name = footprint_name.replace(f"oomp_{owner}_{library}_", "")    
                    pass
                
                
                
                dst = f"c:/gh/oomlout_oomp_footprint_doc/footprints/{owner}/{library}/{footprint_name}"

                #copy all files in source directory inclusion subfodlers to dst directory using shutil
                
                if not os.path.exists(dst) or overwrite:
                    #print(f"Copying {src} to {dst}")
                    #copy all
                    #shutil.copytree(directory, dst, dirs_exist_ok=True)
                    file_list = []
                    file_list.append("readme.md")
                    file_list.append("working_600.png")
                    file_list.append("working.png")
                    file_list.append("working_kicad_pcb_3d_600.png")
                    file_list.append("working_kicad_pcb_3d_140.png")
                    file_list.append("working_kicad_pcb_3d.png")
                    file_list.append("working_kicad_pcb_3d_back_140.png")
                    file_list.append("working_kicad_pcb_3d_back.png")
                    file_list.append("working_kicad_pcb_3d_front_140.png")
                    file_list.append("working_kicad_pcb_3d_front.png")
                    file_list.append("working.yaml")
                    file_list.append("working.kicad_mod")
                    #make directory if it doesn't exist
                    if not os.path.exists(dst):
                        os.makedirs(dst)
                    for file in file_list:
                        src_file = f"{directory}/{file}"
                        dst_file = f"{dst}/{file}"
                        if os.path.exists(src_file):
                            if not os.path.exists(dst_file) or overwrite:
                                
                                shutil.copy(src_file, dst_file)
                        else:
                            pass
                            #print(f"file not found: {src_file}")


                    pass
                else:
                    #print(f"Skipping {src} to {dst}")
                    pass


                pass
                
                #print a dot for progress
                count += 1
                if count % 100 == 0:
                    print(".", end="", flush=True)
                if count % 2000 == 0:
                    print(f"count: {count}  ")
                if count % 5000 == 0:
                    #push doc to git
                    import oom_kicad
                    oom_kicad.push_to_git(repo_directory = "c:/gh/oomlout_oomp_footprint_doc/", count=count )
    import oom_kicad
    oom_kicad.push_to_git(repo_directory = "c:/gh/oomlout_oomp_footprint_doc/", count=count )

                
            







if __name__ == '__main__':
    main()