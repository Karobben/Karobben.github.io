---
toc: true
url: convert
covercopy: © DALLE 3
priority: 10000
date: 2023-12-25 17:16:09
title: "ImageMagick: convert"
ytitle: "ImageMagick: convert"
description: "ImageMagick: convert"
excerpt: "ImageMagick is a versatile open-source tool for image manipulation, capable of reading and writing over 200 image file formats. Renowned for its flexibility, it allows users to efficiently perform a wide array of image transformations, including resizing, format conversion, and special effects, either programmatically or via command line. Ideal for batch processing and on-the-fly image manipulation, ImageMagick is widely employed in web development, graphic design, and photography."
tags: [Linux, Scripting, bash, CLI Tools, Image]
category: [Linux, Software]
cover: "https://imgur.com/0e2Zc1v.png"
thumbnail: "https://imgur.com/0e2Zc1v.png"
---

Documentation: [imagemagick.org](https://imagemagick.org/script/command-line-tools.php)

The `convert` command in Linux is a part of the ImageMagick suite, a powerful toolset for image manipulation. This command allows you to convert between different image formats, resize images, change image quality, and perform a wide variety of other image transformations.

Here are a few basic examples of what you can do with the `convert` command:

1. **Converting an Image Format:**
   To convert a JPEG image to a PNG, you would use:
```bash
convert image.jpg image.png
```

2. **Resizing an Image:**
   To resize an image to a specific width and height (e.g., 100x100 pixels), you can use:

```bash
# based on the pixel of x*y 
convert original.jpg -resize 100x100 resized.jpg
# based on the ratio 
convert original.jpg -resize 30% reduced.jpg
# based on the ratio of x*y
convert original.jpg -resize 50%x30% reduced.jpg
```

3. **Changing Image Quality:**
   To change the quality of a JPEG image, useful for reducing file size, use:
```bash
convert original.jpg -quality 85 compressed.jpg
```

4. **Combining Multiple Images:**
To combine multiple images into one, for instance, side by side:
```bash
convert image1.jpg image2.jpg +append combined.jpg
```

5. **Converting a PDF to an Image:**
To convert a PDF file to a series of images, you can use:
```bash
convert document.pdf document.png
```

6. **Creating an Animated GIF:**
To create an animated GIF from a series of images:
```bash
convert -delay 20 -loop 0 frame1.png frame2.png frame3.png animated.gif
```

These examples are just the tip of the iceberg in terms of what ImageMagick's `convert` command can do. It's a very powerful tool with a wide array of options and capabilities. For more detailed information, you can check the manual page (`man convert`) or the official ImageMagick documentation.


## Other Functions You May Want to Know

Certainly! Here are examples demonstrating various capabilities of ImageMagick:

1. **Image Composition:**
   Overlay one image on top of another (watermark):
```bash
convert background.jpg watermark.png -gravity center -composite output.jpg
```

2. **Color Manipulation:**
   Convert an image to grayscale:
```bash
convert original.jpg -colorspace Gray grayscale.jpg
```

3. **Cropping:**
   Crop an image to a 100x100 pixel square starting at (50,50):
```bash
convert original.jpg -crop 100x100+50+50 cropped.jpg
```

4. **Rotating and Flipping:**
   Rotate an image by 90 degrees:
```bash
convert original.jpg -rotate 90 rotated.jpg
```

5. **Blurring and Sharpening:**
   Apply a Gaussian blur:
```bash
convert original.jpg -blur 0x8 blurred.jpg
```

6. **Drawing:**
   Draw a red rectangle:
```bash
convert original.jpg -fill none -stroke red -draw "rectangle 10,10 50,50" output.jpg
```

7. **Format Conversion:**
   Convert an image to a different format (e.g., PNG to GIF):
```bash
convert image.png image.gif
```

8. **Handling Transparency:**
  Make the white background of an image transparent:
```bash
convert original.jpg -transparent white output.png
```

9. **Image Annotation:**
Add text to an image:
```bash
convert original.jpg -pointsize 24 -fill black -annotate +50+50 'Sample Text' output.jpg
```

10. **Special Effects:**
   Add a shadow to an image:
```bash
convert original.jpg \( +clone -background black -shadow 60x5+10+10 \) +swap -background none -layers merge +repage shadow.jpg
```

11. **Image Optimization:**
   Optimize an image for the web (reduce file size):
```bash
convert original.jpg -strip -interlace Plane -gaussian-blur 0.05 -quality 85% optimized.jpg
```

12. **Batch Processing:**
   Resize all PNG images in a directory (example in a bash loop):
```bash
for img in *.png; do convert "$img" -resize 50% "resized_$img"; done
```

13. **Image Analysis:**
   Get image information (format, dimensions, etc.):
```bash
identify -verbose image.jpg
```

14. **Creating Thumbnails:**
   Generate a thumbnail:
```bash
convert original.jpg -thumbnail 100x100 thumbnail.jpg
```

15. **Morphing and Transforming:**
   Morph between two images:
```bash
convert image1.jpg image2.jpg -morph 10 morph_output.jpg
```

These commands showcase the versatility of ImageMagick. Remember to adjust the file names and parameters according to your specific needs. The ImageMagick documentation provides more detailed information and examples for these and other features.

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
