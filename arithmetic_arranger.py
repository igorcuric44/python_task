import re


def arithmetic_arranger(list):
	try:
		lenx=len(list)
		if lenx>5:
  			raise Exception("Error: Too many problems.")


		
		print(lenx)
		print()
		
		pet1=re.split(' ',list[1])
		
		
		strx=""
		leftx=""
		strp1=""
		strp2="";strp3="";strp4=""
		for i in range(0,lenx):
			
			
			try:
				petx=re.split(' ',list[i])
				leftx=petx[0]
				signx=petx[1]
				rightx=petx[2]
				if signx=="*" or signx=="/":
					raise Exception("Error: Operator must be '+' or '-'.")
				
				if len(leftx)>4 or len(rightx)>4:
					raise Exception("Error: Numbers cannot be more than four digits.")
			
				if len(leftx)>4 or len(rightx)>4:
					raise Exception("Error: Numbers cannot be more than four digits.")
				
				match1=re.search(r'[A-Za-z]+',leftx)
				match2=re.search(r'[A-Za-z]+',rightx)
				
				if bool(match1) or bool(match2):
					raise Exception("Error: Numbers must only contain digits.")
				
				if signx=="+":
					result=int(rightx)+int(leftx)
				else:
					result=int(leftx)-int(rightx)
				
				
				if leftx>rightx:
					letz=len(leftx)
					rightx=signx+" "*letz+rightx
				else:
					letz=len(rightx)
					rightx=signx+" "+rightx
					
				
				
				stri="{0:>15}"
				strp1=strp1+stri.format(leftx)
				strp2=strp2+stri.format(rightx)
				strp3=strp3+stri.format("-"*len(rightx))
				strp4=strp4+stri.format(result)
				
			except Exception as error1:
				print(error1)
				
		print(strp1)
		print(strp2)
		print(strp3)
		print(strp4)
	# Value of Exception is stored in error
	except Exception as error:
		print(error)

arithmetic_arranger(["32 + 698","3a01 - 2","45 + 43","123 * 49","99999 - 2"])
