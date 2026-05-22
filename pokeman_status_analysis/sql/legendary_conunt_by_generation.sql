SELECT
    generation,
    COUNT(*) AS legendary_count
FROM `your-project-id.pokemon_analytics_dev.analytics_pokemon`
WHERE legendary = TRUE
GROUP BY generation
ORDER BY generation;