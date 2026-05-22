SELECT
    generation,
    type_1,
    AVG(attack) AS avg_attack
FROM `your-project-id.pokemon_analytics_dev.analytics_pokemon`
WHERE generation = 1
GROUP BY generation, type_1
ORDER BY avg_attack DESC;