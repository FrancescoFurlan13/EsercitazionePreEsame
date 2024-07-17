from database.DB_connect import DBConnect
from model.genes import Gene


class DAO():
    @staticmethod
    def getLoc():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT c.Localization 
                    FROM classification c 
                    ORDER BY c.Localization ASC
                    """
            cursor.execute(query)

            for row in cursor:
                result.append(row['Localization'])
            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def getLocInter():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT LEAST(c1.Localization, c2.Localization) AS Localization1, 
                        GREATEST(c1.Localization, c2.Localization) AS Localization2, 
                        COUNT(DISTINCT i.Type) AS InteractionTypeCount
                    FROM interactions i 
                    JOIN classification c1 ON i.GeneID1 = c1.GeneID 
                    JOIN classification c2 ON i.GeneID2 = c2.GeneID 
                    WHERE c1.Localization != c2.Localization 
                    GROUP BY Localization1, Localization2
                    """
            cursor.execute(query)

            for row in cursor:
                result.append((row['Localization1'], row['Localization2'], row['InteractionTypeCount']))
            cursor.close()
            cnx.close()
        return result




