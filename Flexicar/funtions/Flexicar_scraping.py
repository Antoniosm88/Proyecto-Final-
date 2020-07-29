from Concat_funtion.py import concat

def FlexicarScraping(tipo):
    #URL=f'https://www.flexicar.es/coches-segunda-mano/#precio_to/{presupuesto}/'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver',options=options) 
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.get(tipo)
    precio= autos = driver.find_elements_by_xpath('//*[@id="listadocoches"]')
    cochesBuenos= [e.text for e in precio]
    for e in cochesBuenos:
        ok=e.split("\n")
    droplist=['Previous','Next',"IVA deducible"]
    cleanList=[e for e in ok if e not in droplist]
    CleanList=[]
    for e in cleanList:
        if not "desde" in e:
             CleanList.append(e)
    priceWithoutDiscount=CleanList[0::4]
    priceWithDiscount=CleanList[1::4]
    model=CleanList[2::4]
    cleanColumn=CleanList[3::4]
    for e in cleanColumn:
        ok=e.split("\n")
    cleanColumn2=[e.split("\n") for e in cleanColumn]
    ok2=[]
    for e in cleanColumn2:
        for i in e:
            ok2.append(i.split())
    Año=[e[0] for e in ok2]
    Combustible=[e[2] for e in ok2]
    combustiblesucio=[re.findall(r"([$D-H](\w+))",e) for e in Combustible]
    combustiblesucio=[list(item) for sublist in combustiblesucio for item in sublist]
    combustible=[item for sublist in combustiblesucio for item in sublist]
    gas=[]
    for e in combustible:
        if e == 'Hibrido':
            gas.append(e)
        elif e == "Diesel":
            gas.append(e)
        elif e == "Gasolina":
            gas.append(e)
        elif e == "Electrico":
            gas.append(e)
        elif e == "GLP":
            gas.append(e)
    df = pd.DataFrame({
                   'priceWithDiscount': priceWithDiscount,
                     'Model' : model,
                     'Combustible': gas,
                     'Año': Año,
                     'cleanToSplit': cleanColumn
                  })
    df1 = pd.DataFrame(df.cleanToSplit.str.split(' ',4).tolist(),
                                 columns = ["Año1","KM","3","Ciudad","nan"])
    result = pd.concat([df, df1], axis=1, sort=False)
    flexicar = result.drop(["cleanToSplit",'Año1','3'], axis=1)
    np_concat = np.vectorize(concat)
    flexicar['Ciudad'] = np_concat(flexicar['Ciudad'], flexicar['nan'])
    flexicar = flexicar.drop(['nan'], axis=1)
    
    
    return flexicar.sort_values(by='Año', ascending=[True])