def main():
    file = input("File name: ").strip().lower()

    if hasExtension(file) == True:
        ext = getExtension(file)

        match ext:
            case "gif" | "png":
                print(f"image/{ext}")
            case "jpg" | "jpeg":
                print(f"image/jpeg")
            case "pdf":
                print(f"application/{ext}")
            case "txt":
                print("text/plain")
            case "zip":
                print(f"application/{ext}")
            case _ :
                print("application/octet-stream")


    else :
        print("application/octet-stream")






def getExtension(file):

    dot = []
    dot = file.split('.')
    

    if (len(dot) > 2):
        ext = dot[-1]
        return ext

    #fileName = file.removesuffix(f'.{ext}')


    else:
        _ , ext  = file.split('.')
        return ext



def hasExtension(file):
    isDotExist = file.find(".")
    if isDotExist > 0:
        return True





main()




