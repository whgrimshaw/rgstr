# rgstr
NFC based registration system for schools

Year 13 A level project. 
v.1 Uses an NFC card to sign in and out of the database register.


LIBRARY RGSTRCONNECT
SUB readconfig(configfile,section='mysql'):
	parser<-ConfigParser()
	parser.read(configfile)
	db<-{}
	if parser has section ("section"):	
		items=parser.items(section)
		for item in items:
			db[item[0]]<-item[1]
		endfor
	else:
		print Error
	endif
	return db
endsub

SUB databaseconnect(configfile):
	db_config<-readconfig(configfile)
	try:
		print Connecting
		conn<-MySQLConnection(**db_config)
		
		if connected:
			print Connected
			return conn
		else:
			print Failure
		endif
	except:
		print (Error)
endsub
