from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

class Facility:


    db= 'giftanon'
    

    def __init__(self,data):

        self.facility_id  = data["facility_id"]        
        self.facility_name = data["facility_name"]
        self.organization = data["organization"]
        self.address1 = data["address1"]
        self.address2 = data["address2"]
        self.phone :data["phone"]
        self.city = data["city"]
        
            

    @classmethod
    def create_facility(cls):
        query = ("INSERT facility_id `facility_name`,organization,address1,address2,phone,city  VALUES (%(facility_id)s, %(facility_name)s,%(organization)s,%(address1)s,%(address2)s,%(phone)s,%(city)s)")
        result = connectToMySQL(Facility.db).query_db(query)

        return result
    


    @classmethod
    def get_all_facilities(cls,):
        query = ("SELECT * from facilities")
        results = connectToMySQL(Facility.db).query_db(query)

        all_facilities=[]

        if results:

            for row in results:
                facility = cls(row)
                all_facilities.append(facility)
            print(results)
            return all_facilities        
        return results
    

    

    # @classmethod
    # def get_all_bins(cls):
    #     query = "SELECT * FROM bins"
    #     results = connectToMySQL(Bin.DB).query_db(query)

    #     all_bins=[]

    #     if results:

    #         for row in results:
                
    #             member= cls(row)
    #             all_bins.append(member)
    #         return all_bins
    #     return results
    

    # @classmethod
    # def get_one_bin(cls,id ):

    #     query = "SELECT * FROM bins where bin_id = %(bin_id)s"        
    #     result = connectToMySQL(Bin.DB).query_db(query,id)   
    #     print(result)
    #     return cls(result[0])
      