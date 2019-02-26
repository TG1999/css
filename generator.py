import pdfkit
import pandas as pd
import datetime
from jinja2 import Template
import pdfkit
import datetime
now = datetime.datetime.now()
df = pd.DataFrame([
        {'package': 'PEPTize', 'student': 'Yashvant Singh', 'level': 'Level 1'},
        {'package': 'PlaceMe Mechanical', 'student': 'Rajeev Kumar', 'level': 'Level 2'},
        {'package': 'N2N Python', 'student': 'Gaurav Singh', 'level': 'Level 2'},
        {'package': 'PEPTize', 'student': 'Rakesh Sharma', 'level': 'Level 3'},
    ])
f = open("./templates/index.html", "r")
template = Template(f.read())
for index,row in df.iterrows():
    options = {'orientation': 'Landscape'}
    x=template.render(student=row['student'],level=row['level'],package=row['package'],certdate=now.date())
    pdfkit.from_string(x,'./output/out'+str(index)+'.pdf',options=options)

