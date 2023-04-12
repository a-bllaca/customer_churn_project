CREATE TABLE default.customer_churn_data
(
`InvoiceNo` String,
`StockCode` Nullable(String),
`Description` Nullable(String),
`Quantity` Nullable(Int64), 
`InvoiceDate` DateTime,
`UnitPrice` Nullable(Float64),
`CustomerID` Nullable(Int64),
`Country` Nullable(String),
`Year` Nullable(Int32),
`Month` Nullable(Int32),
`Quarter` Nullable(Int32),
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(InvoiceDate)
ORDER BY (InvoiceDate, InvoiceNo);
