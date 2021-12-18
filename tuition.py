def tuition():

    tuition=8000
    for year in range(5) :
        tuition=tuition+tuition*(3/100)
        print(f'You must pay {tuition:.2f} $ tuition for Year {year+1}')
tuition()      