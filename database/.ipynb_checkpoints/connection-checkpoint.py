import pyodbc

print([x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')])

db_file = r"D:\_DC\CS_DWH\COPA_CS_Promoter_YTW_20181111.mdb"

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ=D:\_DC\DWH\Sales_ALL_Final_FY1718.mdb;'
    )
cnn = pyodbc.connect(conn_str)
cursor = cnn.cursor()

for table_obj in cursor.tables(tableType='TABLE'):
    tbl = table_obj.table_name
    print("table: ", tbl)
    columns =  [column.column_name for column in cursor.columns(table=tbl)]
    print("table columns: \n", columns)
    print("\n***********************************************************\n")

columns = ['PostMonth', 'WeekNo', 'PostDate', 'MainOrganization', 'Organization', 'Branch', 'SubBranch', 'Territory', 
'Location', 'SalesSubTeam', 'SalesTeam', 'VBEZ', 'SalesName', 'Division', 'Perc', 'BU', 'Division2', 'BU2', 'GBK', 'AKZ', 
'ProjectNo', 'ControllingArea', 'CompanyCode', 'CreatedByUserAccount', 'CreatedByUserName', 'ConsolidationFlag', 
'DataSourceFlag', 'ExportFlag', 'ModeOfPayment', 'Currency', 'ContractNo', 'CustomerNumber', 'CustomerEnglishName', 
'CustomerChineseName', 'DistributionName', 'ImportChannel', 'Ship_to_party', 'Ship_to_party_English_Name', 
'Ship_to_party_Chinese_Name', 'EndUser', 'EndUserEnglishName', 'EndUserChineseName', 'Distributor', 'SAGReferenceNumber', 
'OrderEntryDate', 'ActualDeliveryDate', 'OrderValue_OrderReceived_RMB', 'OrderValue_Turnover_RMB', 'OrderValue_OOH_RMB', 
'ChannelInfo', 'SPVInfo', 'SPRNumber', 'CompanyName', 'SOCreatedondate', 'Payment_terms', 'AssignType', 'SAPOrEBook', 
'AssignedCustomerNo', 'AssignedCustomerName', 'BuyerCNOC', 'SoldToPartyCustomerType', 'AssignedCustomerType', 'AssignSourceCNOC', 
'Territory2', 'SPO_Ref_No']

sql = """
SELECT PostMonth, Organization, SUM(OrderValue_OrderReceived_RMB)
FROM t
WHERE PostMonth in ({})
GROUP BY PostMonth, Organization
""".format('"1", "2"')
cursor.execute(sql)
row = cursor.fetchone()
print(row)
print("\n***********************************************************\n")

rows = cursor.fetchall()
for row in rows:
    print(row)
