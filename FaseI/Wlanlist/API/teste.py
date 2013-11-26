import winWlanApi as winWlanAPI


if __name__ == '__main__':
    
    import time,os
    
    while True:
        time.sleep(1)
        os.system('cls')
        cenas = winWlanAPI.get_BSSI()
        print cenas