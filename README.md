# Content_based_image_retrieval
Extract features from images 🖼️ in the form of color correlogram and compare each against that of the query image.

The main purpose: is to retrieve similar images from a large database given a query image.  

Steps:  
  
In off-line stage: the system automatically extracts  features of each image in the database  and stores  them  in the features database (images are represented with feature vectors).  

In on-line stage:

User input a query image to the system.  

The similarity is measured between the feature vector of the query image and the feature vectors of the images in the database.  

Finally, the system returns the images that  are most similar to the query image (Images with high similarity scores are retrieved). 

features extraction : Extract some useful features from the query image: Texture features based on the correlogram matrix are extracted (the correlogram method is developed from scratch, no need for libraries) 

This method allows us to compare images based on their content. 

What role does computer vision play in AI? 

Computer Vision is a subfield of Artificial intelligence (AI). Computer vision is the process of teaching computers to understand and collect data from the visual environment, such as graphics. Therefore, AI technology is used by computer vision in order to address complicated challenges such as image analysis, object identification, and other similar issues. 
