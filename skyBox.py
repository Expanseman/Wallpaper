from PIL import Image, ImageDraw, ImageFont
import random

class Settings:
	def __init__(self, res, palette):
		self.res = res
		style = 'fonts/Courier Prime Code.ttf'
		size = int((res[1]+res[0])/150)
		self.font = ImageFont.truetype(style, size)
		self.palette = palette

class Shape:
	def __init__(self, coordinates, color):
		self.leftTop = coordinates[0]
		self.rightBot = coordinates[1]
		self.coordinates = coordinates
		self.color = color

def paintRectangle(image, settings, shape):

	draw = ImageDraw.Draw(image)
	fontx = shape.rightBot[0] - (6 * settings.font.size)
	fonty = shape.leftTop[1] + (1.75 * settings.font.size)
	draw.rectangle(shape.coordinates, fill=shape.color)
	#draw.text((fontx, fonty), text=shape.color.upper(), color='white', font=settings.font)
	del draw
	return image


def paintCircle(image, settings, shape):
	draw = ImageDraw.Draw(image)
	fontx = shape.rightBot[0] - (6 * settings.font.size)
	fonty = shape.leftTop[1] + (1.75 * settings.font.size)
	draw.ellipse(shape.coordinates, fill=shape.color)
	#draw.text((fontx, fonty), text=shape.color.upper(), color='white', font=settings.font)
	del draw
	return image

def desertSunset(image, settings):
	xLeft = 0
	xRight = settings.res[0]
	yUpper = 0
	yLower = settings.res[1]

	sky = Shape(coordinates=((xLeft, yUpper), (xRight, yLower)), color=settings.palette[0])
	image = paintRectangle(image=image, settings=settings, shape=sky)


	r = 100
	sun = Shape(coordinates=((150-r, 150-r), (150+r, 150+r)), color=settings.palette[1])
	image = paintCircle(image=image, settings=settings, shape=sun)

	yUpper = int(settings.res[1]/4)*3
	sand = Shape(coordinates=((xLeft, yUpper), (xRight, yLower)), color=settings.palette[-1])
	image = paintRectangle(image=image, settings=settings, shape=sand)
	return image

def create(settings):

	number = 0
	image = Image.new('RGB', settings.res)
	
	image = desertSunset(image=image, settings=settings)

	image.save('images/out.png')
	image.show()

def main():
	res = [(750, 1334), (1280, 720), (1920, 1080), (3840, 2160)]

	style = 'fonts/Courier Prime Code.ttf'

	bla_tur = ['#99b898', '#fecea8', '#ff847c', '#e84a5f', '#2a363b']
	tur_pin = ['#ef4566', '#f69a9a', '#f9cdae', '#c8c8a9', '#83ae9b']
	pur_ora = ['#ee4540', '#c72c41', '#801336', '#510a32', '#2d142c']
	bla_pin = ['#a7a7a7', '#ce547d', '#e01f60', '#494949', '#363636']
	blu_pin = ['#f8b195', '#f67280', '#c06c84', '#6c5b7b', '#355c7d']
	
	nat0 = ['#f1f0a2', '#d1ee48', '#a7b2ff', '#2b44ff', '#2a66b3']
	nat1 = ['#31384f', '#4f597d', '#727ea7', '#a1a9c4', '#d0d4e2']
	nat2 = ['#d0d4e2', '#a1a9c4', '#727ea7', '#4f597d', '#31384f']

	wp = Settings(res=res[1], palette=blu_pin)

	create(wp)

if __name__ == '__main__':
	main()