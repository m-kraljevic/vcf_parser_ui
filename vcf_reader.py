import allel
import os

def get_vcf_files(directory):
    vcf_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".vcf"):
            vcf_files.append(filename)
    return vcf_files

vcf_folder = ''
files = get_vcf_files(vcf_folder)

partialMatches = []
perfectMatches = []

mutations_of_interest = [
]


matchCount = 0

for ind, file in enumerate(files):
    path = vcf_folder + file
    vcf_file = allel.read_vcf(path)
    
    for index, chromosome in enumerate(vcf_file['variants/CHROM']):
        ref = vcf_file['variants/REF'][index]
        alt = vcf_file['variants/ALT'][index][0]
        pos = vcf_file['variants/POS'][index]
        data = (chromosome, 
            pos,
            ref,
            alt )
        
        for mutation in mutations_of_interest :
            if mutation[:2] == (chromosome, pos) :
                matchCount += 1
                if mutation == data :
                    perfectMatches.append(data)
                    print("full match")
                else :
                    partialMatches.append(data)
                    print("partial match")
                    
print("%d matches found" % matchCount)