# PEY Assessment README

I changed the file into a text file since it was easier for me to work with.
The first step in completing this coding task was to parse the data and I noticed that most of the variables followed a certain pattern in the raw file, like how the DIs were on every 7th line and how every BPr was on the last line or 10th.
I then parsed the data according to these patterns and also parsed it according to if every 10 lines contained a certain string by noticing how every string is seperated by the semicolon.

After gathering all the strings into a variable, I then made a "final" data list which contained a list of tuples where each tuple contained information about a data point including the 4 variables.
I then created a dataframe using this list through the pandas library. Afterwards, I have all the data I needed in the data frame and I simply used matplotlib to graph the scatter plot as desired.