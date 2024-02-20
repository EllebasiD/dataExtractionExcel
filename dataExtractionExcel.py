import pandas as pd


# Read myData.xlsx Excel file
df = pd.read_excel(r"myData.xlsx")

# Display all the data from myData.xlsx Excel file
print("* Tableau Excel du fichier myData.xlsx :")
print(df)
print()

# Display the names of the solar system elements if they have an atmosphere and the composition of it
atmosphere_df = df[df['Atmosphère'] != "Inconnu"] 
print("* Noms des éléments du système solaire et de la composition de leur atmosphère s'ils en ont une :")
print(atmosphere_df[["Nom", "Atmosphère"]])
print()

# Display percentage of the solar system elements with hydrogen-containing atmospheres among those with an atmosphere
atmosphere_df_nb = len(atmosphere_df)
hydrogen_atmosphere_nb = len(df[df['Atmosphère'].str.contains("Hydrogène")])
percentage_nb = int(hydrogen_atmosphere_nb / atmosphere_df_nb * 100)
print("* Pourcentage d'éléments du système solaire dont l'atmosphère contient de l'hydrogène parmi ceux qui possèdent une atmosphère : ", percentage_nb, " %")

