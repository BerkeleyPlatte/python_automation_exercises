import os, re

print('What folder are we looking at?  Please specifiy full filepath:')

folder_path = input()
dirListing = os.listdir(folder_path)
nums = []
for each in dirListing:
    nums.append(int(re.findall(r'\d+', each)[0]))
MissingNos = []
working_nums = sorted(nums)
for i in range(len(working_nums[1:])):
    if working_nums[i] - working_nums[i - 1] != 1:
        MissingNos.append(working_nums[i])

# finding the numbers adjacent to those missing, as opposed to the missing
# ones themselves, accounts for the possibility of more than one missing in
# a row

print(MissingNos)