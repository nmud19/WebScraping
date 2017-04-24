import pandas as pd
df = pd.read_json("ans3.json")
df2 = pd.read_json("testv1/full3.json")
# df["product_name2"] = df.product_name.apply(lambda x: "/" + x)
# print(df2.product_link.iloc[0])
df2.product_link = df2.product_link.apply(lambda x: x.split("/")[1])
# print(df2.head())
orignal = df.product_name.tolist()
new = df2.product_link.tolist()
print(len(new), len(orignal))
print(len(set(orignal)))
flag = 0
count = 0
for o in orignal :
	for i in new:
		if o==i :
			flag = 1
			break
	count+=1
	if flag == 0:
		print("found")
	print(count, flag)
	if flag !=1:
		print("orignal : ", o, "new : ", i)
		flag = 0
# for i in range(0, len(new))