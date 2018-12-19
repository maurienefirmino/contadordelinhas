# encoding: utf-8

import os
import sys

#pegando o parametro
for param in sys.argv :
    param_path = param
    

#funcao que conta linhas de arquivos
def line_count(fname):
	return sum(1 for line in open(fname))

#funcao que recebe um caminho e conta as linhas de todos os arquivos
def paste_count(path):
	count = 0
	files = os.listdir(path)

	for f in files:
		#não contando arquivos de conf que tem ponto, tirando a pasta vendor e storage do laravel
		if f[0] == '.' or f == 'vendor' or f == 'storage':
			continue
		#incrementado cada linha para o contador total

		#testando se é arquivo
		if(os.path.isfile(path+'/'+f)):
			print f+' - Arquivo'
			#caso for, realiza a contagem
			count += line_count(path+"/"+f)

		else:
			#caso não for, entra na pasta e conta os arquivos de dentro
			print f + ' - Pasta'
			count += paste_count(path+"/"+f)

	return count


print 'Carregando, aguarde...'
print 'Seu projeto tem '+ str(paste_count(param_path))+' linhas de codigo'    