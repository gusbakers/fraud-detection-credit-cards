USE WAREHOUSE FRAUD_WH;
USE DATABASE FRAUD_DETECTION;
USE SCHEMA RAW;

CREATE OR REPLACE TABLE TRANSACTIONS (
    TRANSACTION_AMOUNT      FLOAT         COMMENT 'Transaction amount in USD',
    HOUR_OF_DAY             INTEGER       COMMENT 'Hour when transaction occurred (0-23)',
    DAY_OF_WEEK             INTEGER       COMMENT '0=Monday, 6=Sunday',
    IS_WEEKEND              INTEGER       COMMENT '1 if Saturday or Sunday',
    IS_ONLINE               INTEGER       COMMENT '1 if online transaction',
    MERCHANT_CATEGORY       VARCHAR       COMMENT 'Type of merchant',
    CUSTOMER_AGE            INTEGER       COMMENT 'Age of the cardholder',
    ACCOUNT_AGE_DAYS        INTEGER       COMMENT 'How old is the account in days',
    TRANSACTIONS_LAST_24H   INTEGER       COMMENT 'Number of transactions in last 24 hours',
    AVG_TRANSACTION_AMT     FLOAT         COMMENT 'Customer historical average amount',
    AMOUNT_VS_AVG_RATIO     FLOAT         COMMENT 'How much this txn deviates from average',
    DISTANCE_FROM_HOME      FLOAT         COMMENT 'Distance from home in km',
    FAILED_ATTEMPTS         INTEGER       COMMENT 'Failed attempts before this transaction',
    IS_FOREIGN_TRANSACTION  INTEGER       COMMENT '1 if transaction is from another country',
    IS_FRAUD                INTEGER       COMMENT '0=Legitimate, 1=Fraud',
    INGESTION_TS            TIMESTAMP     DEFAULT CURRENT_TIMESTAMP()
);
