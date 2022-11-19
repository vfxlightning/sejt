from PIL import Image

program = {
    '000': '0',
    '001': '1',
    '010': '0',
    '011': '1',
    '100': '1',
    '101': '0',
    '110': '1',
    '111': '0'
}

ROWS = 500
COLS = 500

history = [{0}]

for i in range(0, ROWS - 1):
    history.append(set())
    for j in range(-COLS, COLS):
        if program[''.join(['1' if j - 1 in history[-2] else '0', '1' if j in history[-2] else '0', '1' if j + 1 in history[-2] else '0'])] == '1':
            history[-1].add(j)

img = Image.new('RGB', (COLS * 2, ROWS), "white")
for row, cols in enumerate(history):
    for col in cols:
        img.putpixel((col + COLS, row), (0, 0, 0))

img.save("im.png", "png")
