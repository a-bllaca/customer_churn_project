/*
	Run the queries separately.
*/
INSERT INTO default.customer_churn_data SELECT
`InvoiceNo` ,
`StockCode` ,
`Description` ,
`Quantity` , 
`InvoiceDate` ,
`UnitPrice` ,
`CustomerID` ,
`Country` 
FROM url('https://raw.githubusercontent.com/a-bllaca/customer_churn_project/main/final_formated_data2.csv', 'CSVWithNames');


INSERT INTO default.customer_churn_data SELECT
`InvoiceNo` ,
`StockCode` ,
`Description` ,
`Quantity` , 
`InvoiceDate` ,
`UnitPrice` ,
`CustomerID` ,
`Country` 
FROM url('https://raw.githubusercontent.com/a-bllaca/customer_churn_project/main/final_formated_data1.csv', 'CSVWithNames');