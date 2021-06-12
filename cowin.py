from cowin_api import CoWinAPI


co=CoWinAPI()



def init():
		print("1.SEARCH BY DISTRICT\n2.SEARCH BY PINCODE\n")
		ch=int(input("Enter your choice : "))
		
		if(ch==1):
			my_state=input("Enter the name of the state : ")
			my_dis=input("Enter the name of the district : ")
			date=input("Enter the date to be searched for (dd-mm-yyyy) : ")
			age=int(input("Enter minimum age (or 0 if no filter in age) : "))
			#pin=input("Enter the pincode : ")
			st_list=co.get_states()['states']
			for i in st_list:
				if (i.get("state_name")).upper()==my_state.upper():
					myst_id=i.get("state_id")
					break
			dist_dict=co.get_districts(myst_id)
			dist_list=dist_dict['districts']
			for i in dist_list:
				if (i.get("district_name")).upper()==my_dis.upper():
					mydis_id=str(i.get("district_id"))
					break
			if age==0:
				av_cent=co.get_availability_by_district(mydis_id,date)
			else:
				av_cent=co.get_availability_by_district(mydis_id,date,age)
			print_avail(av_cent['centers'],date)
		else:
			pin=input("Enter the pincode : ")
			date=input("Enter the date to be searched for (dd-mm-yyyy) : ")
			age=int(input("Enter minimum age (or 0 if no filter in age) : "))
			if age==0:
				av_cent=co.get_availability_by_pincode(pin,date)
			else:
				av_cent=co.get_availability_by_pincode(pin,date,age)
			
			print_avail(av_cent['centers'],date)

def print_avail(centers,date):
		print("\n\t\tAVAILABLE CENTERS : \n")
		num=1
		for i in centers:
			print(i['center_id'])
			sess=i['sessions']
			for j in sess:
				if j['date']==date :
					req_sess=j
			#print(sess)
			print(f"{num}.{i['name']}\n  {i['address']},{i['block_name']} PIN:{i['pincode']}\n    SLOTS AVAILABLE : {req_sess['available_capacity']}\n    VACCINE         : {req_sess['vaccine']}\n    TIME            : {i['from']} to {i['to']}\n    FEE TYPE        : {i['fee_type']}\n    MINIMUM AGE     : {req_sess['min_age_limit']}")
			
			print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			num=num+1
			
	
	
	


def main():
	print("\n\n\t\tCOVID VACCINATIONS SLOT AVAILABILITY CHECKER\n")
	init();
	print("\n\t\tVisit https://www.cowin.gov.in for further registration\n")

if __name__ =='__main__':
	main()
	
	
	

