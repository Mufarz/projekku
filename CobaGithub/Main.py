#INTERGER
print("====INTERGER====")
data_interger=20

data_float=float(data_interger)
data_string=str(data_interger)
data_boolean=bool(data_interger) #akan false jika nilai int=0
print("data:",data_float,"bertipe:",type(data_float))
print("data:",data_string,"bertipe:",type(data_string))
print("data:",data_boolean,"bertipe:",type(data_boolean))

#FLOAT
print("====FLOAT====")
data_float=15.7

data_interger=int(data_float)
data_string=str(data_float)
data_boolean=bool(data_float) #false jika value = 0
print("data:",data_interger,"bertipe:",type(data_interger))
print("data:",data_string,"bertipe:",type(data_string))
print("data:",data_boolean,"bertipe:",type(data_boolean))

#STRING
print("====STRING====")
data_string="10" #kalau dalam bentuk teks, int dan float akan error. Boolean selalu True kecuali kosong.

data_interger=int(data_string) #harus angka
data_float=float(data_string) #harus angka
data_boolean=bool(data_string) #akan false jika value kosong
print("data:",data_interger,"bertipe:",type(data_interger))
print("data:",data_float,"bertipe:",type(data_float))
print("data:",data_boolean,"bertipe:",type(data_boolean))

#BOOLEAN
print("====BOOLEAN====")
data_bool=True

data_interger=int(data_bool) #jika desimal akan dibulatkan ke bawah
data_float=float(data_bool)
data_string=str(data_bool)
print("data:",data_interger,"bertipe:",type(data_interger))
print("data:",data_float,"bertipe:",type(data_float))
print("data:",data_string,"bertipe:",type(data_string))

print(data_bool)