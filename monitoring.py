import pymysql

host = "127.0.0.1"
port = 6533
database = "nvision"
username = "admin"
password = "qwer1234"

conn = pymysql.connect(host=host,  user=username, password=password, db=database, port=port)
cursor = conn.cursor(pymysql.cursors.DictCursor)

dailyInspectionHistoriesCountQuery = "select H.customerId, C.name, H.inspectionId, I.name,  H.result, H.historiesCount from ( select customerId, inspectionId, result, count(IID) as historiesCount from InspectionHistories where inspectionDate BETWEEN '2023-05-23 00:00:00' AND '2023-05-23 23:59:59' GROUP BY inspectionId,result order by customerId, inspectionId ) H LEFT OUTER JOIN Customers C ON H.customerId = C.id LEFT OUTER JOIN Inspections I ON H.inspectionId = I.id"

cursor.execute(dailyInspectionHistoriesCountQuery)
dailyInspectionHistoriesRows = cursor.fetchall()
print(dailyInspectionHistoriesRows[0])

inspectionDiscriptionQuery = "select I.customerId, C.name , Map.id as InspectionMappingId, I.id as InspctionId, I.name as InspectionName, M.id as ModelId, M.name as ModelName, S.id as SubpartId, S.name as SubpartName, S.yoloID, S.isPositive, S.numObjects, S.inUse, S.threshold, S.useHistogram  from InspectionMappings Map LEFT OUTER JOIN Inspections I ON Map.inspectionId = I.id LEFT OUTER JOIN Models M ON Map.modelId = M.id LEFT OUTER JOIN Subparts S ON M.id = S.modelId LEFT OUTER JOIN Customers C ON C.id = I.customerId  ORDER BY I.customerId,I.id,M.id,S.id"

print("-----------------------------------")

cursor.execute(inspectionDiscriptionQuery)
inspectionDiscriptionRows = cursor.fetchall()
print(inspectionDiscriptionRows[0])




conn.close()
