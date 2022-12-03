while True:
    q= input(' To Add contact press(a)  To Search a contact press(s)  To Quit press(q)')
    if q=='a':
        with open('contact.txt', 'a')as f:
            name=input('name: ')
            phone=input('phone: ')
            f.writelines((name,' : ',phone,'\n'))
    elif q=='s':
        with open('contact.txt' ,'r') as f:
            search=input('Search: ')
            for i in f:
                if search in i:
                         print(i)
    else:
        break
                         
                     
