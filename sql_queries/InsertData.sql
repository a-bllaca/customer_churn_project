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
`Country`,
`year`,
`month`,
`quarter` 
FROM url('https://raw.githubusercontent.com/a-bllaca/customer_churn_project/main/csv_files/output1.csv', 'CSVWithNames');


INSERT INTO default.customer_churn_data SELECT
`InvoiceNo` ,
`StockCode` ,
`Description` ,
`Quantity` , 
`InvoiceDate` ,
`UnitPrice` ,
`CustomerID` ,
`Country`,
`year`,
`month`,
`quarter` 
FROM url('https://raw.githubusercontent.com/a-bllaca/customer_churn_project/main/csv_files/output2.csv', 'CSVWithNames');
