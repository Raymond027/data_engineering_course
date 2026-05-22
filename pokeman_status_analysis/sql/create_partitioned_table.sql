CREATE OR REPLACE TABLE `your-project-id.pokemon_analytics_dev.analytics_pokemon`
PARTITION BY RANGE_BUCKET(generation, GENERATE_ARRAY(1, 10, 1))
CLUSTER BY type_1, legendary
AS
SELECT
    CAST(`#` AS INT64) AS id,
    Name AS name,
    `Type 1` AS type_1,
    `Type 2` AS type_2,
    CAST(HP AS INT64) AS hp,
    CAST(Attack AS INT64) AS attack,
    CAST(Defense AS INT64) AS defense,
    CAST(`Sp. Atk` AS INT64) AS sp_atk,
    CAST(`Sp. Def` AS INT64) AS sp_def,
    CAST(Speed AS INT64) AS speed,
    CAST(Generation AS INT64) AS generation,
    CAST(Legendary AS BOOL) AS legendary
FROM `your-project-id.pokemon_analytics_dev.raw_pokemon`;