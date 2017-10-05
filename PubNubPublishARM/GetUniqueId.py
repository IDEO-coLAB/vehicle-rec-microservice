# File : GetUniqueId.py
# Subprogram to generate a unique id for Pubnub message
# Author: Sooraj Bopanna

import uuid

def GenerateId():
	unique_id=uuid.uuid1()
	str_id=str(unique_id)
	return str_id
	

