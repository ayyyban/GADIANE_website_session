import duckdb



output = duckdb.sql("""
    COPY (     
        
        SELECT 

        DISTINCT *,

        SPLIT_PART(browser_os, '|', 1) AS browser, 
        SPLIT_PART(browser_os, '|', 2) AS os,
        
        TRIM(device_type) AS clean_DT,

        CONCAT(customer_id, ' ', os) AS customer_os,

        session_id,
        COALESCE(session_quality_score, 0) AS session_quality_score
        
        FROM 'bronze.parquet'
    )
    TO 'silver.parquet'
    (FORMAT PARQUET);
""")
output.show()



