import pdfkit
import pandas as pd
import datetime
from jinja2 import Template
import pdfkit
# from slugify import slugify
df = pd.DataFrame([
        {'package': 'PEPTize', 'student': 'Yashvant Singh', 'level': 'Level 1'}
        # {'package': 'PlaceMe Mechanical', 'student': 'Rajeev Kumar', 'level': 'Level 2'},
        # {'package': 'N2N Python', 'student': 'Gaurav Singh', 'level': 'Level 2'},
        # {'package': 'PEPTize', 'student': 'Rakesh Sharma', 'level': 'Level 3'},
    ])
import base64
img=''
with open("./static/images/Background.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    img=str
ht='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<link href='https://fonts.googleapis.com/css?family=Montserrat:400,500,600,800' rel='stylesheet'>
		<link rel='stylesheet' href='./static/styles.css'>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<title>Perfectice - Certificate</title>
	</head>
	<body>
		<div id="background">
			<div id="Background">
				<img class ="img" src="https://user-images.githubusercontent.com/34160672/53386713-5207a600-39a9-11e9-8df8-74b605edf1bd.jpg">
				<span class="main">CERTIFICATE</span>
				<span class="main1">OF COMPLETION</span>
				<span class="content1">This certificate is hereby presented to </span>
				<span class="name">{{student}}</span>
				<span class="content2">for successfully completing <b>{{level}} of {{package}}</b> assessed by Perfectice</span>
				<span class="date">{{certdate}}</span>
				<span class="footer">To validate or download the certificate visit https://lpu.myperfectice.com/cert/</span>
			</div>
		</div>
 </body>
 </html>
 '''
template = Template(ht)
x=template.render(student=df['student'].values[0],level=df['level'].values[0],package=df['package'].values[0],certdate='ab',img=img)
pdfkit.from_string(x,'./output/out.pdf')

