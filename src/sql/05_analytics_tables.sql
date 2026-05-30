USE SCHEMA ANALYTICS;

CREATE OR REPLACE TABLE FEATURES_FOR_ML AS
SELECT
    -- Features numéricas
    TRANSACTION_AMOUNT,
    HOUR_OF_DAY,
    DAY_OF_WEEK,
    IS_WEEKEND,
    IS_ONLINE,
    CUSTOMER_AGE,
    ACCOUNT_AGE_DAYS,
    TRANSACTIONS_LAST_24H,
    AVG_TRANSACTION_AMT,
    AMOUNT_VS_AVG_RATIO,
    DISTANCE_FROM_HOME,
    FAILED_ATTEMPTS,
    IS_FOREIGN_TRANSACTION,
    AMOUNT_ZSCORE,

    -- Features categóricas como número
    CASE MERCHANT_CATEGORY
        WHEN 'grocery'       THEN 0
        WHEN 'retail'        THEN 1
        WHEN 'restaurant'    THEN 2
        WHEN 'gas'           THEN 3
        WHEN 'travel'        THEN 4
        WHEN 'entertainment' THEN 5
        WHEN 'healthcare'    THEN 6
    END AS MERCHANT_CATEGORY_CODE,

    CASE TIME_OF_DAY
        WHEN 'dawn'      THEN 0
        WHEN 'morning'   THEN 1
        WHEN 'afternoon' THEN 2
        WHEN 'evening'   THEN 3
    END AS TIME_OF_DAY_CODE,

    CASE ACCOUNT_AGE_CATEGORY
        WHEN 'new'         THEN 0
        WHEN 'recent'      THEN 1
        WHEN 'established' THEN 2
        WHEN 'veteran'     THEN 3
    END AS ACCOUNT_AGE_CODE,

    -- Target
    IS_FRAUD AS LABEL

FROM FRAUD_DETECTION.STAGING.TRANSACTIONS_CLEAN;

-- Verificar
SELECT COUNT(*) FROM FRAUD_DETECTION.ANALYTICS.FEATURES_FOR_ML;
-- Esperado: 100000
