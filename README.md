# Mapping Terrorism in the Wakhan Corridor Region

![image](assets/corridorNYTimes.jpg)

## Wakhan Corridor

The Wakhan Corridor is a narrow strip of land that extends from Eastern Afghanistan to China.
The territory was first marked in an 1893 agreement between Sir Henry Mortimer Durand (representing Britain) and Amir Abdur Rahman Khan (representing Afghanistan).
The territory served as an important buffer between British India and the Russian Empire.

In the modern era, the Wakhan Corridor is primed to be a strategic resource for whichever country controls it.

China has identified the region's importance in its Belt and Road infrastrucure projects. The corridor will aid their connections to the Middle East and the new deep water ports that they are building along the Gulf of Oman and Arabian Sea. Perhaps they desire to run a natural gas pipeline connecting Pakistan, Afghanistan, and the broader Middle East, through the Wakhan Corridor and into Xinjiang.

India does not want a strong relationship between Pakistan and China. India already disputes large border areas with both Pakistan and China, and the Wakhan Corrider could potentially cut them off from Central Asia should China move aggressively.

Russia maintains strong relationships with Tajikistan and has military instillations with thousands of troops in the region.

Pakistan stands to gain heavily from infrastructure investment in the Wakhan Corridor because once the Chinese break through that region trade will increase and foreign development throughout the country will skyrocket.

All of the countries near the Wakhan Corridor (save Afghanistan itself) are nuclear powers. Any instability in the region could set off a chain reaction that leads to conflict. Border skirmishes among the countries in the area are already commonplace, and have the potential to grow into much larger geopolitical strife that impacts the entire world.

## Terrorism

University of Maryland's National Consortium for the Study of Terrorism and Responses to Terrorism maintains the Global Terrorism Database. It is the most comprehensive data store of terrorist incidents from 1970 to 2018.

> "The GTD defines a terrorist attack as the threatened or actual use of illegal force and violence by a non-state actor to attain a political, economic, religious, or social goal through fear, coercion, or intimidation. In practice this means in order to consider an incident for inclusion in the GTD, all three of the following attributes must be present: 1) The incident must be intentional – the result of a conscious calculation on the part of a perpetrator. 2) The incident must entail some level of violence or immediate threat of violence -including property violence, as well as violence against people. 3) The perpetrators of the incidents must be sub-national actors. The database does not include acts of state terrorism."

The database contains entries of every known terrorist attack. These entries have detailed information about the location of the attack, the type of attack, the terrorist group, number of casualties, media reports, and much more.

## Mapping

The Global Terrorism database is extremely detailed. This makes web mapping difficult because the end user will not be able to dynamically render very much informtation without long load times. To remedy this I trimmed  excess information out of my data. I only included the following countries: India, China, Tajikistan, Afghanistan, and Pakistan. I also removed all unnecessary information fields and eliminated all data before 2000. This helped load times, but they were still very large, so I decided to only dynamically render the terrorist incidents closest to the Wakhan Corridor. For all other incidents I use pre-rendered map feature layer tiles to improve loading times. The reason I wanted to include all of the data for each country even in a limited capacity is for additional context.

I use the leaflet js mapping library with tiles generated from mapbox customized basemaps and tiles generated with the QMapTiles plugin for QGIS. The project, including the web map, is hosted on Github.
