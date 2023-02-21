import geopandas as gpd


go = gpd.read_file("GO_Municipios_2021/GO_Municipios_2021.shp")
go.head()
#data = gpd.read_file(go)
#print(go)

abadiania = go[go.NM_MUN == 'Abadiânia'].reset_index(drop=True)
ax2 = abadiania.plot()
ax2.set_title('Setores Censitários - Cidade de Abadiânia');

print(abadiania)