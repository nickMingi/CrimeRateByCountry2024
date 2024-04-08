import pandas as pd

###################################################################################
########################## UNITED STATES ##########################################
###################################################################################

crimeCountData = pd.read_csv(f"./Data/UnitedStates/US_Arrests_by_offense_age_race.csv", encoding="cp949")

selected_columns = ["Offenses","All races"]

revisedCrimeCount = crimeCountData[selected_columns]

revisedCrimeCount_index = revisedCrimeCount.set_index("Offenses")

noNull_Crime_Index = revisedCrimeCount_index.fillna("0")

noNull_Crime_Index["All races"] = [x.replace(',','') for x in noNull_Crime_Index["All races"]]
noNull_Crime_Index["Count"] = pd.to_numeric(noNull_Crime_Index["All races"])

refined_index_crime = noNull_Crime_Index["Count"]

theft_crime = refined_index_crime.loc[["Robbery","Burglary","Larceny-theft","Motor vehicle theft"]]

murder_crime = refined_index_crime.loc[["Murder and nonnegligent manslaughter"]]

assault_crime = refined_index_crime.loc[["Aggravated assault","Simple assault"]]

final_data = {"Count": [murder_crime.sum(), 0, theft_crime.sum(), assault_crime.sum()]}

final_df = pd.DataFrame(final_data,index=["살인","강간","절도","폭행"])

PoliceCountData = pd.read_csv(f"./Data/UnitedStates/NumberOfPoliceOfficer_US.csv", encoding = "cp949")

PopulationData = pd.read_csv(f"./Data/UnitedStates/US_Population.CSV", encoding = "cp949")

selected_columns = ["Year","Population"]

revisedPopulationData = PopulationData[selected_columns]

revisedPopulationData = revisedPopulationData.set_index("Year")
PoliceCountData = PoliceCountData.set_index("Year")

revisedPopulationData["Population"] = [x.replace(',','') for x in revisedPopulationData["Population"]]
revisedPopulationData["PopulationCount"] = pd.to_numeric(revisedPopulationData["Population"])

numericPopulationData = revisedPopulationData.drop(columns = ["Population"])

combinedPolicePopulation = pd.merge(PoliceCountData,numericPopulationData,left_index=True,right_index=True,how='outer')

finalPolicePopulation = combinedPolicePopulation.loc[2020]

finalPolicePopulationData = pd.DataFrame({
    "Count" : [finalPolicePopulation["NumberOfPoliceOfficer"],finalPolicePopulation["PopulationCount"]]
}, index = ["총경찰관수","총인구수"]
)

cctvData = pd.read_csv(f"./Data/UnitedStates/US_CCTV.csv", encoding = "cp949")

selected_columns = ["City","# of CCTV Cameras"]

revisedcctvData = cctvData[selected_columns]

revisedcctvData["# of CCTV Cameras"] = [x.replace(',','') for x in revisedcctvData["# of CCTV Cameras"]]
revisedcctvData["Count"] = pd.to_numeric(revisedcctvData["# of CCTV Cameras"])
finalcctvData = pd.DataFrame({
    "Count" : [revisedcctvData["Count"].sum(),finalPolicePopulation["PopulationCount"]]
}, index = ["총CCTV수","총인구수"]
)

recidivismData = pd.read_csv(f"./Data/UnitedStates/Recidivism_US.csv", encoding = "cp949")

selected_columns = ["State","Recidivism Rate"]
revisedRecidivism = recidivismData[selected_columns]
revisedRecidivism["Recidivism Rate"] = [x.replace('%','') for x in revisedRecidivism["Recidivism Rate"]]
revisedRecidivism["Rate"] = pd.to_numeric(revisedRecidivism["Recidivism Rate"])
finalrecidivismData = pd.DataFrame({
    "Count" : [revisedRecidivism["Rate"].mean()]
}, index = ["재범률"]
)
finalrecidivismData['Count'] = finalrecidivismData['Count'].round(1)

unitedStates_df = pd.concat([final_df,finalPolicePopulationData,finalcctvData,finalrecidivismData])

unitedStates_df = unitedStates_df.loc[~unitedStates_df.index.duplicated(keep="last")]

unitedStates_df = unitedStates_df.rename(columns={'Count': 'US'})

print(unitedStates_df)

###################################################################################
########################## KOREA ##################################################
###################################################################################

koreacrimeCountData = pd.read_csv(f"./Data/SouthKorea/대한민국_경찰청_전국 범죄 발생 및 검거 현황_20211231.csv", encoding = "cp949")

selected_columns = ["범죄소분류","발생"]

korearevisedCrimeCount = koreacrimeCountData[selected_columns]

korearevisedCrimeCount_index = korearevisedCrimeCount.set_index("범죄소분류")

koreanoNull_Crime_Index = korearevisedCrimeCount_index.fillna("0")

koreanoNull_Crime_Index["Count"] = pd.to_numeric(koreanoNull_Crime_Index["발생"])

koreatheft_crime = koreanoNull_Crime_Index.loc[
[
"강도",
"준강도",
"특수강도",
"준특수강도",
"강도상해·치상",
"강도살인·치사",
"해상강도(살인·치사·상해·치상)",
"인질강도",
"강도강간",
"(특수·인질·해상)강도(상습)",
"특가법(강도)",
"특가법(강도상해재범)",
]
]

koreamurder_crime = koreanoNull_Crime_Index.loc[
[
"살인",
"영아살해",
"존속살해",
"촉탁·승낙살인",
"자살교사·방조",
"위계·위력·촉탁·승낙살인",
"특가법(보복살인등)",
"아동학대처벌법(아동학대살해)"
]
]

koreaassault_crime = koreanoNull_Crime_Index.loc[
[
"폭행",
"폭행(상습)",
"폭행치상",
"폭행치사",
"특수폭행",
"특수폭행(상습)",
"특수폭행치상",
"특수폭행치사",
"존속폭행",
"존속폭행(특수)",
"존속폭행(상습)",
"존속폭행치상",
"존속폭행치사",
"특가법(운전자폭행등)",
"특가법(보복폭행등)",
"특가법(보복범죄등)",
"아동학대처벌법위반(상습폭행)",
"폭력행위등처벌에관한법률위반(상습)",
"폭력행위등처벌에관한법률위반(공동)",
"폭력행위등처벌에관한법률위반(집단,흉기등)",
"폭력행위등처벌에관한법률위반(상습집단,흉기등)",
"폭력행위등처벌에관한법률위반(야간·공동)",
"폭력행위등처벌에관한법률위반(야간집단흉기등)",
"폭력행위등처벌에관한법률위반(단체등의구성·활동)",
"폭력행위등처벌에관한법률위반(단체등의[상습·공동·상습특수])",
"폭력행위등처벌에관한법률위반(단체등의이용·지원)",
"폭력행위등처벌에관한법률위반(우범자)"
]
]

korearape_crime = koreanoNull_Crime_Index.loc[
[
"강간",
"강간(상습)",
"준강간",
"준강간(상습)",
"강간상해·치상",
"강간살인·치사",
"미성년자간음(심신미약자)",
"업무상위력에의한간음",
"친족관계에의한강간",
"장애인에대한강간·간음",
"청소년에대한강간·간음",
"미성년자의제강간",
"13세미만미성년자강간·간음",
"특수강간(준)",
"주거침입강간",
"절도강간",
"특수강도강간",
"아동학대처벌법위반(상습강간·간음)",
"16세미만아동·청소년간음"
]
]

koreafinal_data = {"Count": [koreamurder_crime["Count"].sum(), korearape_crime["Count"].sum(), koreatheft_crime["Count"].sum(),
                        koreaassault_crime["Count"].sum()]}

koreafinal_df = pd.DataFrame(koreafinal_data,index=["살인","강간","절도","폭행"])

###################################################################################
########################## JAPN ###################################################
###################################################################################

japancrimeCountData = pd.read_csv(r'./Data/Japan/crime_data_japan_2022.csv', encoding="cp949")

selected_columns = ["Offenses","Reported cases"] # Offenses, Reported cases 열 선택
japanrevisedCrimeCount = japancrimeCountData[selected_columns]

japanrevisedCrimeCount_index = japanrevisedCrimeCount.set_index("Offenses") # Offenses 열 df 인덱스로 설정

japanrevisedCrimeCount_index["Reported cases"] = japanrevisedCrimeCount_index["Reported cases"].astype(str).str.replace(',', '')
# Reported cases 열에서 쉼표 제거, 문자열 형식으로 변환

japanrevisedCrimeCount_index["Count"] = pd.to_numeric(japanrevisedCrimeCount_index["Reported cases"])
# Reported cases 열숫자 형식으로 변환

japanrefined_index_crime = japanrevisedCrimeCount_index["Count"]
# df에서 Count 열 추출

japanfinal_data = {"Count": japanrevisedCrimeCount_index["Count"].tolist()}
# revisedCrimeCount_index의 Count 열 값을 리스트로 가지는 final_data 생성

japanfinal_df = pd.DataFrame(japanfinal_data, index=["살인", "강간", "절도", "폭행"])

japanPoliceCountData = pd.read_csv("./Data/Japan/NumberOfPolice_2020.csv")

print(japanPoliceCountData)

'''selected_columns = ["number","total population"]

cnt = japanPoliceCountData[selected_columns]
cnt["total population"].fillna(0, inplace=True)

japanpolice_cnt = pd.DataFrame({"Count": [cnt["number"].sum(),
                                    cnt["total population"].sum()]},
                          index=["총경찰관수", "총인구수"])
print(japanpolice_cnt)'''

###################################################################################
########################## FRANCE##################################################
###################################################################################

df1 = pd.read_csv('./Data/France/프랑스 살인 (연도별).CSV',encoding ='cp949')
df1.drop([1,2,3,4,0,5,6,7,8,9,10], axis = 0, inplace=True)
df = df1.rename(columns = {'per 100000' : 'Count'})
a = 64531444/100000
df = df.mul(a)
df = df.drop(columns = ['Year'])
df = round(df)

df2 = pd.read_csv('./Data/France/프랑스 강간 (연도별).CSV', encoding = 'cp949')
df2.drop([0,1,2,3], axis = 0 , inplace = True)
df2 = df2.drop(columns = ['year','15-17 years','Over 18 years'])
df2 = df2.drop(df2.columns[0],axis=1)
df2 = df2.rename(columns = {'Total' : 'Count'})

df3 = pd.read_csv('./Data/France/프랑스 절도 (연도별).CSV', encoding = 'cp949')
df3 = df3.drop(columns = ['Year'])
df3 = df3.replace(to_replace=r'[,]',value='',regex=True)
df3['Count'] = df3.apply(lambda x: pd.to_numeric(x,errors='coerce')).sum(axis=1).round(1)
df3 = df3.drop([0,1,2,3,4,5])
df3 = df3.drop(columns = ['Theft offences with weapons'])
df3 = df3.drop(columns = ['Theft offences without violence'])
df3 = df3.drop(columns = ['Theft offences with violence but without  weapons'])

middle_df = pd.concat([df, df2, df3])
francefinal_df = pd.DataFrame({ "Count" :{"살인" : middle_df.iloc[0][0], "강간" : middle_df.iloc[1][0] , "절도" : middle_df.iloc[2][0],"폭행": 0}})
francefinal_df = pd.DataFrame(francefinal_df, index =['살인','강간','절도','폭행'])
print(francefinal_df)

'''francepopulation = pd.read_csv('./Data/France/france_population.CSV', encoding = 'cp949')
francepopulation = francepopulation.drop([1,2,3])
print(francepopulation)'''

francepolice = pd.read_csv('./Data/France/프랑스 총 경찰수 (연도별).CSV', encoding = 'cp949')
francepolice = francepolice.drop([0,1,2,3,4,5,6,7,8])
print(francepolice)
'''police_population = pd.concat([police,population])
police_population = police_population.drop(columns = 'Year')
police_population = pd.DataFrame(police_population, index = ['총경찰관수','총인구수'])
police_population = police_population.rename(columns = {'Population' : 'Count'})
police_population = police_population.drop(columns = 'Number of police officers')
police_population = pd.DataFrame({ 'Count' : { '총경찰관수' : 154547 , '총인구수':64531444}})
print(police_population)'''

'''cctv = pd.read_csv('./Data/France/amount of cctv.CSV' , encoding = 'cp949')
cctv = cctv.drop(columns = '순위')
cctv = cctv.drop([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18])
cctv_population = pd.concat([cctv,population])
cctv_population = cctv_population.drop(columns = '나라')
cctv_population = cctv_population.drop(columns = 'Year')
cctv_population = pd.DataFrame(cctv_population , index = ['총CCTV수','총인구수'])
cctv_population = cctv_population.drop(columns = 'CCTV 개수')
cctv_population = cctv_population.rename(columns = {'Population' : 'Count'})
cctv_population = pd.DataFrame({'Count' : {'총CCTV수': 1650000 ,'총인구수' :64531444}})
print(cctv_population)'''

francerecidivism = pd.read_csv('./Data/France/프랑스 재범율 (연도별).CSV', encoding = 'cp949')
francerecidivism = francerecidivism.drop([0,1,2,3,4,5,6,7,8])
francerecidivism = francerecidivism.drop(columns = 'year ')
francerecidivism = pd.DataFrame(francerecidivism, index = ['재범률'])
francerecidivism = francerecidivism.rename(columns = {'recidivism rate' : 'Count'})
francerecidivism = pd.DataFrame({'Count': {'재범률': 14.6}})
print(francerecidivism)

###################################################################################
########################## FINAL ##################################################
###################################################################################

#myFinal_df = pd.concat([final_df,koreafinal_df])
#print(myFinal_df)