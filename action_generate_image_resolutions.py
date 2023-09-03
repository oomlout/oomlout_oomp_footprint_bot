import oom_base



def main():
    #go through all files in symbols/
    import os
    count = 1   
    count2  = 1
    counter = 0
    for root, dirs, files in os.walk("footprints"):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file
                if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                    resolutions = [140,300,600,1000]
                    for resolution in resolutions:
                        #generate the image at this resolution
                        filename = os.path.join(root, name, file)
                        #print(filename)
                        counter = oom_base.generate_image(filename=filename, resolution=resolution)
                        pass
                    count2 += 1
                    count += counter
                    counter = 0
                    #print a dot every 1000 files
                    if count2 % 100 == 0:
                        print(".", end="", flush=True)
                    if count % 1000 == 0:
                        import oom_kicad
                        oom_kicad.push_to_git(count=count )
    oom_kicad.push_to_git(count=count )






if __name__ == '__main__':
    main()