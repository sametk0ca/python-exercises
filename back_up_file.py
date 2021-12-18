def back_up_files():
    f=open('text2.txt')
    back_up=open('back_up_file.txt','w')
    back_up.write(f.read())
    f.close()
    back_up.close()
back_up_files()     