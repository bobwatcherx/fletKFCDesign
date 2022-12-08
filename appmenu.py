from flet import *
from flet import colors

jumbotron = AppBar(
	toolbar_height=90,
	bgcolor="#E3002A",
	title=Row([
		Container(
		padding = padding.all(4),
		border = border.all(3,"white"),
		border_radius = border_radius.all(30),
		content=Text("Location",color="white",size=13)

		),
		Container(
		content=Image(
		src=f"image/kfc.png",
		width=100,
		height=70
		)

		)

		],alignment="spaceBetween")

	)
