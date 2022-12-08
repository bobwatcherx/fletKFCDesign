from flet import *
from data import data_burger,data_drinks,data_twister

burger_list = Column(scroll="auto")
twister_list = Column(scroll="auto")
drinks_list = Column(scroll="auto")

# LOOP BURGER TO APPEND 
for x in data_burger:
	burger_list.controls.append(
		Row([
			Image(
			width=110,
			height=80,
			src=x['images']
				),
			Container(
			content=Column([
			Text(x['title'],size=16,weight="bold"),
			Row([
				Container(
				padding = padding.all(10),
				border = border.all(3,"red"),
				border_radius = border_radius.all(30),
				content=Text(f" + {x['price']}")
					),
				Column([
				Text(x['weight'],size=13,color="grey",
				weight="bold"),
				# FOR LIKE ICON
				Row([
				Icon(name="favorite",color="grey"),
				Text(f"{x['like']} suka",size=15)
					])

					],alignment="start")
				])

				])
			)
			])

		)
# TWISTER LOOP
# LOOP TWISTER TO APPEND 
for x in data_twister:
	twister_list.controls.append(
		Row([
			Image(
			width=110,
			height=80,
			src=x['images']
				),
			Container(
			content=Column([
			Text(x['title'],size=16,weight="bold"),
			Row([
				Container(
				padding = padding.all(10),
				border = border.all(3,"red"),
				border_radius = border_radius.all(30),
				content=Text(f" + {x['price']}")
					),
				Column([
				Text(x['weight'],size=13,color="grey",
				weight="bold"),
				# FOR LIKE ICON
				Row([
				Icon(name="favorite",color="grey"),
				Text(f"{x['like']} suka",size=15)
					])

					],alignment="start")
				])

				])
			)
			])

		)

# DATA DRINK LOOP
# LOOP DRINK TO APPEND 
for x in data_drinks:
	drinks_list.controls.append(
		Row([
			Image(
			width=110,
			height=80,
			src=x['images']
				),
			Container(
			content=Column([
			Text(x['title'],size=16,weight="bold"),
			Row([
				Container(
				padding = padding.all(10),
				border = border.all(3,"red"),
				border_radius = border_radius.all(30),
				content=Text(f" + {x['price']}")
					),
				Column([
				Text(x['weight'],size=13,color="grey",
				weight="bold"),
				# FOR LIKE ICON
				Row([
				Icon(name="favorite",color="grey"),
				Text(f"{x['like']} suka",size=15)
					])

					],alignment="start")
				])

				])
			)
			])

		)

# RENDER TABS MENU
tabs_menu = Tabs(
	# DEFAULT OPEN IS BURGER THEN SELECT 0
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="Burgers",
                content=burger_list
            ),
             Tab(
                text="Twisters",
                content=twister_list
            ),
             Tab(
                text="Drinks",
                content=drinks_list
            ),

         ])
