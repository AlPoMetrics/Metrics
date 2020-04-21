import pandas as pd 
import xml.etree.ElementTree as et


tree = et.parse('/Users/alessandropollastri/Desktop/country_data.xml')
root = tree.getroot()

df_cols = ['country', 'neighbor', 'direction', 'number']
rows = []

for country in root.iter('country'):
    this_country = country.get('name')
    for child in country:  
        if child.tag == 'neighbor':
            name = child.attrib.get("name")
            direction = child.attrib.get("direction")
            number = child.text
            rows.append({'country': this_country,
                         'neighbor': name,
                         'direction': direction,
                         'number': number,
                        })
                        

out_df = pd.DataFrame(rows, columns = df_cols)
out_df                        
                        
