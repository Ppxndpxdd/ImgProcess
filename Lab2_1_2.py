import numpy as np
import cv2

image_path = 'cat1.jpg'
image = cv2.imread(image_path)  

new_width = 640
new_height = int(image.shape[0] * (new_width / image.shape[1]))
resized_image = cv2.resize(image, (new_width, new_height))

gamma_values_less_than_one = np.linspace(0, 1, num=10)
gamma_values_greater_than_one = np.linspace(1.2, 3, num=10)

video_filename = 'gamma_comparison_video.mp4'
frame_size = (new_width * 3, new_height)
fps = 5
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, frame_size)

original_with_text = resized_image.copy()
cv2.putText(original_with_text, "Original Image", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

for frame_num, (gamma_less_than_one, gamma_greater_than_one) in enumerate(zip(gamma_values_less_than_one, gamma_values_greater_than_one), start=1):

    adjusted_image_less = ((resized_image / 255.0) ** gamma_less_than_one) * 255
    adjusted_image_less = np.clip(adjusted_image_less, 0, 255).astype(np.uint8)
    
    adjusted_image_greater = ((resized_image / 255.0) ** gamma_greater_than_one) * 255
    adjusted_image_greater = np.clip(adjusted_image_greater, 0, 255).astype(np.uint8)
    
    text_less = f"Frame: {frame_num}, Gamma: {gamma_less_than_one:.2f}"
    image_with_text_less = adjusted_image_less.copy()
    cv2.putText(image_with_text_less, text_less, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    text_greater = f"Frame: {frame_num}, Gamma: {gamma_greater_than_one:.2f}"
    image_with_text_greater = adjusted_image_greater.copy()
    cv2.putText(image_with_text_greater, text_greater, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    comparison_frame = np.hstack((original_with_text, image_with_text_less, image_with_text_greater))
    
    video_writer.write(comparison_frame)

video_writer.release()

print("Video saved as", video_filename)
