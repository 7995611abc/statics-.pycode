import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


# Read the dataset into a Pandas dataframe
df = pd.read_csv("Dataset1.csv")
df.columns = ["Country Name", "Country Code", "Indicator Name", "Indicator Code","1971","1972",	"1973",	"1974",	"1975",	"1976",	"1977",	"1978",	"1979",	"1980", "1981",	"1982",	"1983",	"1984",	"1985",	"1986",	"1987",	"1988",	"1989",	"1990",	"1991",	"1992",	"1993",	"1994",	"1995",	"1996",	"1997",	"1998",	"1999",	"2000",	"2001",	"2002",	"2003",	"2004",	"2005",	"2006",	"2007",	"2008",	"2009",	"2010",	"2011",	"2012",	"2013",	"2014", "2015",	"2016",	"2017",	"2018",	"2019",	"2020",	"2021"]

def Data():
    
    # Read the dataset into a Pandas dataframe
    df = pd.read_csv("Dataset1.csv")
    df.columns = ["Country Name", "Country Code", "Indicator Name", "Indicator Code","1971",	"1972",	"1973",	"1974",	"1975",	"1976",	"1977",	"1978",	"1979",	"1980", "1981",	"1982",	"1983",	"1984",	"1985",	"1986",	"1987",	"1988",	"1989",	"1990",	"1991",	"1992",	"1993",	"1994",	"1995",	"1996",	"1997",	"1998",	"1999",	"2000",	"2001",	"2002",	"2003",	"2004",	"2005",	"2006",	"2007",	"2008",	"2009",	"2010",	"2011",	"2012",	"2013",	"2014", "2015",	"2016",	"2017",	"2018",	"2019",	"2020",	"2021"]
    
    # Line Plot
    df.plot(x="Country Name", legend=True,y=["1971",	"1972",	"1973",	"1974",	"1975",	"1976",	"1977",	"1978",	"1979",	"1980", "1981",	"1982",	"1983",	"1984",	"1985",	"1986",	"1987",	"1988",	"1989",	"1990",	"1991",	"1992",	"1993",	"1994",	"1995",	"1996",	"1997",	"1998",	"1999",	"2000",	"2001",	"2002",	"2003",	"2004",	"2005",	"2006",	"2007",	"2008",	"2009",	"2010",	"2011",	"2012",	"2013",	"2014", "2015",	"2016",	"2017",	"2018",	"2019",	"2020",	"2021"])
    plt.title("Climate Change yearwise ")
    plt.xlabel("Countries")
    plt.xticks(rotation = 90)
    plt.ylabel("Climate Change")
    plt.savefig("Climate CHange")
    plt.figure(figsize=(25, 5))
    plt.show()
    
    # Use the melt function to transform the dataframe
    df_melted = pd.melt(df, id_vars=['Country Name', 'Indicator Name'], var_name='Year', value_name='Value')
    
    # Separate the melted dataframe into two dataframes: one with years as columns and one with countries as columns
    df_by_year = df_melted.set_index(['Country Name', 'Indicator Name', 'Year']).apply(pd.to_numeric, errors='coerce')
    df_by_country = df_melted.set_index(['Indicator Name', 'Country Name', 'Year']).apply(pd.to_numeric, errors='coerce')
    
    # Line Plot for IND
    india_data = df_by_year.loc['India']
    india_data.plot()
    plt.title("Climate Change Trends in IND")
    plt.xlabel("Year")
    plt.xticks(rotation = 90)
    plt.ylabel("Value")
    plt.savefig("Ind.jpg")
    plt.show()

    # Dot Plot for UK
    uk_data = df_by_year.loc['United Kingdom']
    # If 'Year' is part of the MultiIndex
    uk_data = uk_data.reset_index(level='Year')
    plt.figure(figsize=(8, 6))
    plt.scatter(uk_data['Year'], uk_data['Value'], color='green', marker='o')  # You can choose any color
    plt.title("Climate Change Trends in UK (Dot Plot)")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.xticks(rotation=90)
    plt.savefig("UK_dot_plot.jpg")
    plt.show()

    # Bar Chart for US
    us_data = df_by_year.loc['United States']
    # If 'Year' is part of the MultiIndex
    us_data = us_data.reset_index(level='Year')
    plt.figure(figsize=(8, 6))
    plt.bar(us_data['Year'], us_data['Value'], color='red') 
    plt.title("Climate Change Trends in US")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.xticks(rotation=90)
    plt.savefig("US_bar_chart.jpg")
    plt.show()

    return df_by_year, df_by_country
# Example usage of the function to read and transform the dataset
df_by_year, df_by_country = Data()

# Perform basic analysis on the dataframe
print(df_by_country.loc['Population growth (annual %)'].describe())
print(df_by_country.loc['Energy use (kg of oil equivalent per capita)'].describe())

# Calculate correlation between two indicators
population_growth = df_by_country.loc['Population growth (annual %)', :, :]
energy_use = df_by_country.loc['Energy use (kg of oil equivalent per capita)', :, :]
corr = population_growth['Value'].corr(energy_use['Value'])

# Scatter Plot
plt.scatter(population_growth['Value'], energy_use['Value'])
plt.title("Correlation between Population growth and Energy use")
plt.xlabel("Population growth")
plt.ylabel("Energy use")
plt.savefig("scatter Plot")
plt.xticks(rotation = 90)
plt.show()

# Heatmap
fig, ax = plt.subplots(figsize=(10, 6))
corr_matrix = df_by_country.corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', annot_kws={'fontsize': 10}, ax=ax)
plt.title("Correlation Between Indicators")
plt.xlabel("Indicator")
plt.xticks(rotation = 90)
plt.ylabel("Country")
plt.show()
plt.savefig('Climate_change by country')
print(f" Population growth and Energy use Comparison: {corr}")
