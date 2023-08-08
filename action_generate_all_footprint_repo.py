


def main(**kwargs):
    pass
    source_directory = "all_the_kicad_footprints_one_library"
    destination = "c:/gh/oomlout_oomp_footprint_all_the_kicad_footprints"

    import os
    import shutil
    #make destination if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.copytree(source_directory, destination, dirs_exist_ok=True)







if __name__ == '__main__':
    main()