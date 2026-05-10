import os
import struct

res_dir = 'resources'
os.makedirs(res_dir, exist_ok=True)

# Create 89 BMPs
for i in range(1, 90):
    path = os.path.join(res_dir, f'ski32_{i}.bmp')
    width = 32
    height = 32
    row_size = ((24 * width + 31) // 32) * 4
    pixel_data = bytearray()
    for y in range(height):
        for x in range(width):
            pixel_data.extend([0x80, 0x80, 0x80])
        pixel_data.extend(b'\x00' * (row_size - width * 3))
    file_size = 14 + 40 + len(pixel_data)
    with open(path, 'wb') as f:
        f.write(b'BM')
        f.write(struct.pack('<IHHI', file_size, 0, 0, 14 + 40))
        f.write(struct.pack('<IiiHHIIiiII', 40, width, height, 1, 24, 0, len(pixel_data), 2835, 2835, 0, 0))
        f.write(pixel_data)

# Create basic ICO file with one 32x32 icon
ico_path = os.path.join(res_dir, 'iconski.ico')
width = 32
height = 32
bits = 24
row_size = ((bits * width + 31) // 32) * 4
pixel_data = bytearray()
for y in range(height):
    for x in range(width):
        pixel_data.extend([0xff, 0x00, 0x00])
    pixel_data.extend(b'\x00' * (row_size - width * 3))
mask_stride = ((width + 31) // 32) * 4
mask_data = b'\x00' * (mask_stride * height)
info_header = struct.pack('<IiiHHIIiiII', 40, width, height * 2, 1, bits, 0, len(pixel_data) + len(mask_data), 2835, 2835, 0, 0)
with open(ico_path, 'wb') as f:
    f.write(struct.pack('<HHH', 0, 1, 1))
    f.write(struct.pack('<BBBBHHII', width, height, 0, 0, 1, bits, len(info_header) + len(pixel_data) + len(mask_data), 6 + 16))
    f.write(info_header)
    f.write(pixel_data)
    f.write(mask_data)

print('created', len(os.listdir(res_dir)), 'files in', res_dir)
