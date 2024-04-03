import pandas as pd

crimeCountData = pd.read_csv(f"./Data/UnitedStates/US_Arrests_by_offense_age_race.csv", encoding="cp949")

#crimeCountData.info()

selected_columns = ["Offenses","All races"]

revisedCrimeCount = crimeCountData[selected_columns]

revisedCrimeCount.head()

revisedCrimeCount_index = revisedCrimeCount.set_index("Offenses")

revisedCrimeCount_index.head()

noNull_Crime_Index = revisedCrimeCount_index.fillna("0")
noNull_Crime_Index.head()

str(noNull_Crime_Index["All races"].dtype)

noNull_Crime_Index["All races"] = [x.replace(',','') for x in noNull_Crime_Index["All races"]]
noNull_Crime_Index["Count"] = pd.to_numeric(noNull_Crime_Index["All races"])
noNull_Crime_Index.head()

refined_index_crime = noNull_Crime_Index["Count"]
refined_index_crime.head()

noNull_Crime_Index.index

theft_crime = refined_index_crime.loc[["Robbery","Burglary","Larceny-theft","Motor vehicle theft"]]
theft_crime.head()

murder_crime = refined_index_crime.loc[["Murder and nonnegligent manslaughter"]]
murder_crime.head()

assault_crime = refined_index_crime.loc[["Aggravated assault","Simple assault"]]
assault_crime.head()

final_data = {"Count": [murder_crime.sum(), 0, theft_crime.sum(), assault_crime.sum()]}

final_data

final_df = pd.DataFrame(final_data,index=["살인","강간","절도","폭행"])
print(final_df)

