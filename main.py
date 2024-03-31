from PIL import Image
import os
import glob

def compress_image(input_image_path, output_image_path, quality):
    image = Image.open(input_image_path)
    # 이미지를 저장하면서 압축 품질을 설정합니다. (1-100)
    image.save(output_image_path, "JPEG", optimize=True, quality=quality)

# A 폴더의 이미지 파일들을 B 폴더로 압축하여 이동
def compress_and_move_images(source_folder, destination_folder, quality):
    # source_folder 내의 모든 jpg 파일에 대해 반복
    for image_path in glob.glob(os.path.join(source_folder, '*.jpg')):
        # 이미지 파일 이름만 추출
        image_name = os.path.basename(image_path)
        # 목적지 파일 경로 설정
        output_image_path = os.path.join(destination_folder, image_name)
        # 이미지 압축 및 이동
        compress_image(image_path, output_image_path, quality)

source_folder = 'original_images'
destination_folder = 'compressed_images'
compress_and_move_images(source_folder, destination_folder, quality=50)
