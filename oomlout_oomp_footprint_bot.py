import os
import oom_kicad
import oom_markdown

def load_data():
    github_data = "https://github.com/oomlout/oomlout_oomp_footprint_src"

    #make tmp/data directory if it doesn't already exist
    if not os.path.exists("tmp/data/oomlout_oomp_footprint_src"):
        os.makedirs("tmp/data/oomlout_oomp_footprint_src")
    #clone to tmp/
    os.system("git clone " + github_data + " tmp/data/oomlout_oomp_footprint_src")


def copy_data():
    print("Copying data to footprints directory")
    directory_src = rf"tmp/data/oomlout_oomp_footprint_src/footprints_flat"
    directory_dst = rf"footprints"
    #copy the directory with overwite if the file already exists
    import shutil
    shutil.copytree(directory_src, directory_dst, dirs_exist_ok=True)
    print("renaming readme to readme_src.md")
    #rename readme to readme_src.md in all directories in footprint
    count = 0
    for root, dirs, files in os.walk("footprints"):
        for name in dirs:
            #rename readme to readme_src.md
            readme_src = os.path.join(root, name, "readme_src.md")
            readme = os.path.join(root, name, "readme.md")
            #if readme_src exists then delete it
            if os.path.exists(readme_src):
                os.remove(readme_src)
            if os.path.exists(readme):
                os.rename(readme, readme_src)
            count += 1
            #print a dot for progress
            if count % 1000 == 0:
                print(".", end="", flush=True)
    print("Done")

    
    

def open_footprint_window():
    oom_kicad.open_footprint_window()


def make_temporary_library():
    print("Making temporary library")
    #footprint_directory_tmp = "tmp\\footprints.pretty"
    footprint_directory_tmp = "c:/gh/oomlout_oomp_footprint_all_the_kicad_footprints/all_the_kicad_footprints_one_library.pretty"
    #make the tmp directory if it doesn't exist
    if not os.path.exists(footprint_directory_tmp):
        os.makedirs(footprint_directory_tmp)
    #go through one level of directories in tmp 
    counter = 0
    for dir in os.listdir("tmp/data/oomlout_oomp_footprint_src/footprints_flat"):
        #copy working.kicad_mod in each directory to footprints tmp directory but change working.kicad_mod to {direcetory}.kicad_mod
        files_dir = "tmp/data/oomlout_oomp_footprint_src/footprints_flat/" + dir + "/working"
        files = os.listdir(files_dir)
        for file in files:
            if file.endswith(".kicad_mod"):
                filename = os.path.join(files_dir, file)
                #replace // with /
                filename = filename.replace("\\", "/")
                #get directory name its the second to last directory
                directory_name = filename.split("/")[-3]
                #copy to footprints directory using shutil
                import shutil
                src = filename
                dst = footprint_directory_tmp + "/" + directory_name + ".kicad_mod"
                shutil.copyfile(src, dst)
                #print a dot for progress
                counter += 1
                #pritn for every 100
                if counter % 1000 == 0:
                    print(".", end="", flush=True)
    print()
    print("Done")

def generate_readme(**kwargs):
    
    overwrite = kwargs.get("overwrite",False)
    filename = kwargs.get("filename",None)
    #get directory from filename
    directory = os.path.dirname(filename) 
    readme_file = os.path.join(directory,"readme.md")
    print(f"generating readme for {directory}")
    #create a deep copy of kwargs
    import copy
    p2 = copy.deepcopy(kwargs)
    p2["directory"] = directory
    readme = get_readme(**p2)

    #write readme file
    #as unicode
    with open(readme_file, 'w', encoding='utf-8') as text_file:
        text_file.write(readme)


def get_readme(**kwargs):
    directory = kwargs.get("directory","none")

    readme = "# OOMP Footprint  \n"
    import copy
    p2 = copy.deepcopy(kwargs)
    yaml_file = p2.get("directory", "none") + "\\working.yaml"
    if os.path.exists(yaml_file):
        import yaml
        with open(yaml_file, 'r') as stream:
            try:
                yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
            except:
                print("yaml file error")
                readme += "yaml file error"
                return readme
        #if yaml dict is a list then take the first element
        if isinstance(yaml_dict, list):
            yaml_dict = yaml_dict[0]

        ## from repo
        repo = yaml_dict.get("repo", "none")
        repo_name = ""
        repo_owner = ""        
        if repo != "none":
            repo_name = repo.get("name", "none")
            repo_owner = repo.get("owner", "none")
            if repo_owner != "none":
                repo_owner = repo_owner["login"]

        ## from links
        links = yaml_dict.get("links", "none")
        repo_link = ""
        oomp_bot_github = ""
        github_src = ""
        if links != "none":
            repo_link = links.get("github_src", "none")
            github_src = links.get("github_src", "none")
            oomp_bot_github = links.get("oomp_bot_github", "none")

        ## from footprint
        footprint = yaml_dict.get("footprint", "none")
        footprint_name = ""
        footprint_description = ""
        footprint_number_of_pads = ""
        if footprint != "none":
            footprint_name = footprint.get("libraryLink", "none")
            footprint_description = footprint.get("description", "none")
            footprint_number_of_pads = footprint.get("number_of_pads", "none")

        
        oomp_key = yaml_dict.get("oomp_key", "none")
        github_path = yaml_dict.get("github_path", "none")

        p2["repo_name"] = repo_name
        p2["repo_owner"] = repo_owner
        p2["repo_link"] = repo_link
        p2["github_src"] = github_src
        p2["footprint_name"] = footprint_name
        p2["footprint_description"] = footprint_description
        p2["footprint_number_of_pads"] = footprint_number_of_pads
        p2["oomp_key"] = oomp_key
        p2["github_path"] = github_path
        p2["oomp_bot_github"] = oomp_bot_github
        

        p2["readme"] = readme
        readme += get_intro(**p2)
        ###### footprint
        p2["readme"] = readme
        readme += get_footprint(**p2)
        ###### images
        p2["readme"] = readme
        readme += get_images(**p2)



        return readme
    else:
        print( "no yaml file found")
        readme += "no yaml file found"
        return readme

def get_intro(**kwargs):
    name = kwargs.get("name","none")
    footprint_name = kwargs.get("footprint_name","none")
    repo_owner = kwargs.get("repo_owner","none")
    repo_link = kwargs.get("repo_link","none")
    oomp_key = kwargs.get("oomp_key","none")
    readme = ""
    directory = kwargs.get("directory","none")
    ###### introduction

    readme += f'## {footprint_name}  by {repo_owner}  \n'
    readme += f'  \n'
    readme += f'oomp key: {oomp_key}  \n'
    readme += f'  \n'
    repo_link_link = oom_markdown.get_link(link=repo_link)
    readme += f'source repo at: {repo_link_link}  \n'

    return readme

def get_footprint(**kwargs):
    directory = kwargs.get("directory","none")
    footprint_name = kwargs.get("footprint_name","none")
    footprint_description = kwargs.get("footprint_description","none")
    footprint_number_of_pads = kwargs.get("footprint_number_of_pads","none")
    github_path = kwargs.get("github_path","none")
    oomp_key = kwargs.get("oomp_key","none")
    oomp_bot_github = kwargs.get("oomp_bot_github","none")

    readme = "## Footprint  \n"
    ###### board
    image_link = oom_markdown.get_link_image_scale(image="working_kicad_pcb_3d.png",resolution="600")
    readme += f'  \n'
    readme += f'{image_link}  \n'
    image_link = oom_markdown.get_link_image_scale(image="working.png",resolution="600")
    readme += f'  \n'
    readme += f'{image_link}  \n'
    footprint_filename = f'{directory}/working.kicad_mod'
    #oom_kicad.get_footprint_pin_names(filename=footprint_filename)
    table_array = []
    table_array.append(["footprint name", footprint_name])
    table_array.append(["footprint description", footprint_description])
    table_array.append(["number of pads", footprint_number_of_pads])
    table_array.append(["github path", github_path])
    table_array.append(["oomp key", oomp_key])
    table_array.append(["oomp bot github", oomp_bot_github])
    readme+=oom_markdown.get_table(data=table_array)

    return readme

def get_images(**kwargs):
    
    directory = kwargs.get("directory","none")
    readme = "## Images  \n"

    #get all images in directory
    import glob
    images = glob.glob(directory + "\\*.png")
    images += glob.glob(directory + "\\*.jpg")
    images += glob.glob(directory + "\\*.jpeg")
    for image in images:
        #grab the filename split after the last _
        test = image.split("_")[-1]
        digit_test = test[1:3].isdigit()
        if not digit_test:
            just_filename = os.path.basename(image)
            image_link = oom_markdown.get_link_image_scale(image=just_filename)

            readme += f'  \n'
            readme += f'{image_link}  \n'





    return readme


