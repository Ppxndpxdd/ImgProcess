import numpy as np
import cv2

image_path = 'test.jpg'
image = cv2.imread(image_path)

slope_values = np.linspace(0.5, 1.5, num=20)
intercept_values = np.linspace(0, 200, num=20)

video_filename = 'final_comparison_video.mp4'
frame_size = (image.shape[1] * 2, image.shape[0] * 2)
fps = 5
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, frame_size)

for slope_val, intercept_val in zip(slope_values, intercept_values):

    original_image = image.copy()
    
    fixed_slope_adjusted = (image * 1.5) + intercept_val
    fixed_slope_adjusted = np.clip(fixed_slope_adjusted, 0, 255).astype(np.uint8)
    
    changing_slope = (image * slope_val) + 200
    changing_slope = np.clip(changing_slope, 0, 255).astype(np.uint8)
    
    changing_both = (image * slope_val) + intercept_val
    changing_both = np.clip(changing_both, 0, 255).astype(np.uint8)
    
    original_text = "Original Image"
    fixed_slope_text = f"Fixed Slope (1.5) | Intercept: {intercept_val:.2f}"
    changing_slope_text = f"Changing Slope: {slope_val:.2f} | Fixed Intercept (100)"
    changing_both_text = f"Changing Slope & Intercept | Slope: {slope_val:.2f}, Intercept: {intercept_val:.2f}"
    
    cv2.putText(original_image, original_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(fixed_slope_adjusted, fixed_slope_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(changing_slope, changing_slope_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(changing_both, changing_both_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    top_row = np.hstack((original_image, fixed_slope_adjusted))
    bottom_row = np.hstack((changing_slope, changing_both))
    comparison = np.vstack((top_row, bottom_row))
    
    video_writer.write(comparison)

video_writer.release()

print("Video saved as", video_filename)
