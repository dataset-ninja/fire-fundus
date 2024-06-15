The authors created **FIRE: Fundus Image Registration Dataset** for the evaluation of retinal image registration methods. It contains 134 retinal image pairs with the aim of assessing the accuracy of retinal image registration. Additionally, ground truth image point correspondences are provided for each image pair, so that they can be used to validate the accuracy of an image registration algorithm. The dataset could also be utilized for other purposes, such as vessel segmentation and optic disc feature analysis or diagnosis, potentially in a comparative way due to the registration of images.

## Motivation

Fundoscopy allows for non-invasive observation of microvascular circulation, aiding in the diagnosis and monitoring of diseases characterized by vasculopathy, such as diabetes and hypertension. Assessing microcirculation by measuring and monitoring vascular morphology is essential in these cases. Image registration—a technique that aligns a test image to the coordinate frame of a reference image so that corresponding points match in both images—can significantly enhance this process in various retinal imaging applications, including super resolution, mosaicing, and longitudinal studies.

Each of these applications involves image pairs with distinct characteristics. In super resolution, overlapping images are combined to create higher resolution and definition images, enabling more precise measurements. Mosaicing stitches together images to provide a larger field of view (FOV), covering a greater retinal surface area, even with minimal overlap between input images. Longitudinal studies track disease progression or regression by comparing images from different examination sessions.

Despite its importance and practical significance, retinal image registration presents challenges. Image pairs often exhibit variations in illumination, color, and contrast, as well as small overlapping areas. Additionally, structural changes in the retina due to disease progression or remission can complicate registration. Accurate measurements are crucial for medical diagnosis, necessitating effective methods, datasets, and protocols to quantify the accuracy of retinal image analysis methods.

## Dataset description

FIRE comprises a collection of 129 retinal images forming 134 image pairs. Multiple images may be available for a single eye, allowing for various pair combinations. The images were captured using a Nidek AFC-210 fundus camera with a resolution of 2912 × 2912 pixels and a 45° × 45° field of view (FOV). These images were obtained at the Hypertension Unit of the 3rd Department of Internal Medicine, Papageorgiou Hospital, Aristotle University of Thessaloniki, Greece, from 39 male and female patients aged 19-67 during their regular appointments between 2006 and 2015. Written informed consent was obtained prior to data acquisition and processing.

The image pairs are categorized into three types based on their characteristics. Each pair belongs to a single category. Category ***S*** includes 71 image pairs with a large spatial overlap (> 75%) and no visual anatomical differences, making them suitable for super resolution applications. Category ***P*** comprises 49 image pairs, also lacking visual anatomical differences but with a smaller overlap (< 75%), which are useful for mosaicing applications. Category ***A*** consists of 14 image pairs with a large overlap, acquired during different examinations, and featuring visual anatomical differences due to the progression or remission of retinopathy. These differences may manifest as increased vessel tortuosity, microaneurysms, cotton-wool spots, etc., making them ideal for longitudinal studies.

Categories S and P may also include pathological cases affecting the retina's structure, but as these images lack anatomical differences, retinopathy remains unchanged within each pair. All three categories can feature eye shape deformations caused by myopia or hypermetropia.

|                                     | Category S       | Category P | Category A         |
| ----------------------------------- | ---------------- | ---------- | ------------------ |
| # Image pairs                       | 71               | 49         | 14                 |
| Approximate overlap                 | > 75%            | < 75%      | > 75%              |
| Anatomical changes                  | No               | No         | Yes                |
| Indicative registration application | Super Resolution | Mosaicing  | Longitudinal Study |

<span style="font-size: smaller; font-style: italic;">Characteristics of the FIRE dataset image pair categories.</span>

<img src="https://github.com/dataset-ninja/fire-fundus/assets/120389559/048a37bf-3369-4fcc-aee8-b8979929bbf8" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Image pairs from the FIRE dataset. The left column shows a pair from Category S, the second column a pair from Category P, and the two rightmost pairs from Category A. White dots indicate control point locations.</span>

The authors provide ground truth for calculating the registration error in the form of corresponding points between the images in the pair. These are hereafter referred to as control points. The location of a control point j in the reference image is denoted as cj, and the corresponding point in the test image as tj . A registration method takes the points tj as input and maps them to the new coordinates rj. Thus, the rj points are the tj points after registration. If registration is perfect, points cj and rj coincide and their distance (in image pixels) is 0. Ten corresponding points are provided for each image pair. An annotator manually selected these correspondences, locating approximately eight of them towards the edges of the overlapping area and the remaining points towards the center. 

Points were chosen to be widespread across the image, providing a broad coverage of the overlapping surface between images, so that the accuracy across the whole image can be calculated. Given that they were manually selected, points are mainly located on vessels and crossings as they allowed the annotator to provide accurate initial markings, which is a challenging task with uncertain outcome in other image areas that lack image structure. The number of correspondences was selected by balancing the trade-on between the time availability of the annotator, accuracy of annotations, and number of marked images.
