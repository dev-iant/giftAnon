from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

class Categories:


    db= 'giftanon'
    

    def __init__(self,data):

        self.category_id  = data["category_id"]        
        self.category_name = data["category_name"]
        
        
            

    @classmethod
    def create_category(cls):
        query = ("INSERT category_name  VALUES ( %(category_name)s)")
        result = connectToMySQL(Categories.db).query_db(query)

        return result
    


    @classmethod
    def get_all_categories(cls):
        query = ("SELECT * from categories")
        results = connectToMySQL(Categories.db).query_db(query)

        all_categories=[]

        if results:

            for row in results:
                category = cls(row)
                all_categories.append(category)
            print(results)
            return all_categories       
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
      