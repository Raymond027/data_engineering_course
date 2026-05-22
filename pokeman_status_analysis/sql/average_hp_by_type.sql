SELECT
    type_1,
    ROUND(AVG(hp), 2) AS average_hp,
    COUNT(*) AS pokemon_count
FROM `your-project-id.pokemon_analytics_dev.analytics_pokemon`
GROUP BY type_1
ORDER BY average_hp DESC;