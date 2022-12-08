from flet import *
from data import menu_kfc

cardmenu = Row()


for x in menu_kfc:
	cardmenu.controls.append(
		Card(
		elevation=20,
		content=Container(
		bgcolor="white",
		width=150,
		border_radius = border_radius.all(30),
		content=Column([
			Image(
			src=x['image'],
			border_radius = border_radius.all(30),
			width=150,
			height=110,
			fit=ImageFit.CONTAIN
				),
			Container(
			padding = padding.all(10),
			content=Column([
			Text(x['title'],size=16,weight="bold"),
			Text(x['desc'],size=13),

			# FOR PRICE AND BUTTON
			Row([
			Text(x['price'],size=23,weight="bold"),
			IconButton(icon="add")
				],alignment="spaceBetween")
			])
			)

			])	

		)

		)

		)

sectioncard = Container(
	padding = padding.only(top=20),
	bgcolor= "#E3002A",
	content=Column([
	Container(
	margin = margin.only(left=10),
	content=Text("In Restaurant",
		color="white",
		size=30,weight="bold"
		)
	),
	Row([
       cardmenu

		],scroll="auto")

		])

	)