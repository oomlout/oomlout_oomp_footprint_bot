import oomlout_oomp_footprint_bot as oom_ofb




def main():
    oom_ofb.load_data()
    oom_ofb.copy_data()    
    oom_ofb.make_temporary_library()
    #oom_ofb.open_footprint_window()
        ###need to set all layers to print
    #oom_ofb.go_through_directories()






if __name__ == '__main__':
    main()