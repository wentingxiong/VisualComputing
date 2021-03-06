def jaccard_similarity(string_a, string_b):
    # string_a = "China|Scene|Sunny|Forest"
    # string_b = "Germany|Scene|Rainy|Forest"
    string_a_tokens = string_a.split("|")
    string_b_tokens = string_b.split("|")
    intersection = list(set(string_a_tokens) & set(string_b_tokens))
    union = list(set(string_a_tokens) | set(string_b_tokens))
    jaccard_similarity = float(len(intersection)) / float(len(union))
    return jaccard_similarity


import csv
from sim import image_similarity as imsi

dir = "/run/media/liwang/Other/photos/xiphoto/test/"
f = open('%sinfo.csv' % dir, 'rU')
reader = csv.reader(f)
headers = reader.__next__()
print(headers)

column = {}
for h in headers:
    column[h] = []
for row in reader:
    for h, v in zip(headers, row):
        column[h].append(v)

print(column)

dim = len(column['FileName'])

histogram_similarity_matrix = [[0 for x in range(dim)] for x in range(dim)]
cosine_similarity_matrix = [[0 for x in range(dim)] for x in range(dim)]
ghc_similarity_matrix = [[0 for x in range(dim)] for x in range(dim)]

hist_output_file = open('%s/sim_info_hist.csv' % dir, 'w')
hist_writer = csv.writer(hist_output_file)

cosine_output_file = open('%ssim_info_cosine.csv' % dir, 'w')
cosine_writer = csv.writer(cosine_output_file)

ghc_output_file = open('%ssim_info_ghc.csv' % dir, 'w')
ghc_writer = csv.writer(ghc_output_file)

photo_path = dir

for i in range(len(column['FileName'])):
    print(i)
    for j in range(len(column['FileName'])):
        photo1 = photo_path + column['FileName'][i]
        photo2 = photo_path + column['FileName'][j]
        # photo_tag_1 = column['Tags'][i]
        # photo_tag_2 = column['Tags'][j]
        histogram_similarity = imsi.histogram_similarity(photo1, photo2)
        cosine_similarity = imsi.pixel_cosine_similarity(photo1, photo2)
        ghc_similarity = imsi.ghc_similarity(photo1, photo2)
        # similarity = jaccard_similarity(photo_tag_1,photo_tag_2)
        histogram_similarity_matrix[i][j] = histogram_similarity
        cosine_similarity_matrix[i][j] = cosine_similarity
        ghc_similarity_matrix[i][j] = ghc_similarity

hist_writer.writerows(histogram_similarity_matrix)
cosine_writer.writerows(cosine_similarity_matrix)
ghc_writer.writerows(ghc_similarity_matrix)
