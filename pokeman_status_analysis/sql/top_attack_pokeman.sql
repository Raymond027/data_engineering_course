SELECT
    name,
    type_1,
    attack,
    legendary
FROM `your-project-id.pokemon_analytics_dev.analytics_pokemon`
ORDER BY attack DESC
LIMIT 10;