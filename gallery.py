import cv2
import numpy as np
class Gallery:
    def __init__(self, img_path1='images/cmu.jpeg', img_path2='images/cmu.jpeg', img_path3='images/cmu.jpeg',img_path4='images/cmu.jpeg'):
        # self.floor_color = (0xFF, 0xA2, 0xAF)
        self.floor_color = (0x72, 0x7c, 0xA9)
        self.roof_color = (0x90, 0xB8, 0x17)
        self.backwall_color = (0xeb, 0x43, 0x70)
        self.img_path1 = img_path1
        self.img_path2 = img_path2
        self.img_path3 = img_path3
        self.img_path4 = img_path4
    def center_crop(self, image, fixed_height = 500, crop_width = 600):

        # Calculate the scaling factor to resize the image
        scale_factor = fixed_height / image.shape[0]

        # Resize the image
        resized_image = cv2.resize(image, (int(image.shape[1] * scale_factor), fixed_height))

        # Calculate the center coordinates for cropping
        crop_height = fixed_height
        crop_x = int((resized_image.shape[1] - crop_width) / 2)
        crop_y = int((resized_image.shape[0] - crop_height) / 2)

        # Perform the center crop
        cropped_image = resized_image[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]
        return cropped_image


    # Load the images

    def change_perspective(self, image1, image2, x1, y1, x2, y2, x3, y3, x4, y4):
        # Define the four corner points of the region in the first image
        pts1 = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], dtype=np.float32)

        # Define the four corner points of the region in the second image
        pts2 = np.array([[0, 0], [600, 0], [0, 500], [600, 500]], dtype=np.float32)

        # Compute the perspective transform matrix
        matrix = cv2.getPerspectiveTransform(pts2, pts1)

        # Apply the perspective transform to the second image
        transformed_image = cv2.warpPerspective(image2, matrix, (image1.shape[1], image1.shape[0]))

        # Overlay the transformed image onto the first image
        # output = cv2.addWeighted(image1, 1, transformed_image, 1, 0)
        mask = np.zeros_like(image1)
        cv2.fillPoly(mask, [pts1.astype(int)], (255, 255, 255))
        inv_mask = cv2.bitwise_not(mask)
        result = cv2.bitwise_and(image1, inv_mask)
        result = cv2.bitwise_or(result, transformed_image)
        # output = cv2.addWeighted(image1, 1, transformed_image, 0.5, 0)
        # output = cv2.bitwise_and(output, inv_mask) + cv2.bitwise_and(transformed_image, mask)

        return result
    def paint_backwall(self, image, x1, y1, x2, y2, color = (0, 0, 255)):
        
        # Create a mask for the ROI
        mask = np.zeros_like(image)
        cv2.rectangle(mask, (x1, y1), (x2, y2), (255, 255, 255), -1)  # Fill the ROI with white color (255, 255, 255)
        image_with_color = np.where(mask == 255, color, image)
        image_with_color = image_with_color.astype(np.uint8)
        return image_with_color
    def paint_roof_floor(self, image1, x1, y1, x2, y2, x3, y3, x4, y4, color = (0, 0, 255)):
        # Define the four corner points of the region in the first image
        pts1 = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], dtype=np.float32)

        # Define the four corner points of the region in the second image
        pts2 = np.array([[0, 0], [600, 0], [0, 500], [600, 500]], dtype=np.float32)
        # Compute the perspective transform matrix
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
        mask = np.zeros_like(image1)
        cv2.rectangle(mask, (0, 0), (600, 500), (255, 255, 255), -1)  # Fill the ROI with white color (255, 255, 255)
        image_with_color = np.where(mask == 255, color, image1)
        image2 = image_with_color.astype(np.uint8)
        # Apply the perspective transform to the second image
        transformed_image = cv2.warpPerspective(image2, matrix, (image1.shape[1], image1.shape[0]))

        # Overlay the transformed image onto the first image
        output = cv2.addWeighted(image1, 1, transformed_image, 1, 0)
        mask = np.zeros_like(image1)
        cv2.fillPoly(mask, [pts1.astype(int)], color)
        inv_mask = cv2.bitwise_not(mask)
        result = cv2.bitwise_and(image1, inv_mask)
        result = cv2.bitwise_or(result, transformed_image)
        return result

    def plot_gallery(self):
        # image1 = cv2.imread('cat.jpg')
        user_image1 = cv2.imread(self.img_path1)
        user_image2 = cv2.imread(self.img_path2)
        user_image3 = cv2.imread(self.img_path3)
        user_image4 = cv2.imread(self.img_path4)

        background = np.zeros_like(user_image1)

        user_image1 = self.center_crop(user_image1)
        user_image2 = self.center_crop(user_image2)
        user_image3 = self.center_crop(user_image3)
        user_image4 = self.center_crop(user_image4)
        background = self.center_crop(background)

        # background = self.paint_roof_floor(background, 0, 0, 240, 195, 0, 500, 240, 295, color = self.roof_color) # roof
        # output = paint_roof_floor(output,  240, 295, 360, 295, 0, 500, 600, 500, color = (255,0,  0))
        output = self.change_perspective(background, user_image1, 10, 33, 130, 130, 10, 472, 130, 375) 
        output = self.change_perspective(output, user_image2, 150, 141, 230, 207, 150, 359, 230, 293)
        output = self.change_perspective(output, user_image3, 370, 207, 450, 141, 370, 293, 450, 359)
        output = self.change_perspective(output, user_image4, 470, 130, 590, 33, 470, 375, 590, 472)
        output = self.paint_backwall(output, 240, 195, 360, 295, color = self.backwall_color) # backwall
        output = self.paint_roof_floor(output, 0, 0, 600, 0, 240, 195, 360, 195, color = self.roof_color) # roof
        output = self.paint_roof_floor(output, 240, 295, 360, 295, 0, 500, 600, 500, color = self.floor_color) # floor
        # output = self.paint_roof_floor(output, 0, 0, 240, 195, 0, 500, 240, 295, color = self.roof_color)
        return output
    def cv_display(self):
        cv2.imshow('Output', self.plot_gallery())
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def cv_save_image(self):
        cv2.imwrite('gallery.jpg', self.plot_gallery())
# Display the resulting image
g = Gallery()
g.cv_save_image()
# g.cv_display()