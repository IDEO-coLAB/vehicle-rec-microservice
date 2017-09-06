import uuid

def GenerateId():
	unique_id=uuid.uuid1()
	str_id=str(unique_id)
	return str_id
	

