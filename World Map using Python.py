import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

projection = ccrs.PlateCarree()

fig, ax = plt.subplots(subplot_kw={'projection': projection})
ax.set_extent([-180, 180, -90, 90], crs=projection)

ax.add_feature(cfeature.LAND, facecolor='lightgreen')
ax.add_feature(cfeature.OCEAN, facecolor='navy')

ax.gridlines()
plt.show()