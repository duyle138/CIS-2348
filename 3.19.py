#Duy Le 1913048
import math
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area:', wall_area,'square feet')
paint_needed = wall_area / 350
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')
cans_needed = math.ceil(paint_needed)
print('Cans needed:', cans_needed, 'can(s)')
print('')
print('Choose a color to paint the wall:')
print('Cost of purchasing red paint: $', paint_colors['red'])