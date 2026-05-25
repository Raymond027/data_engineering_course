
    
    

select
    pokemon_id as unique_field,
    count(*) as n_records

from "pokemon_db"."analytics_staging"."stg_pokemon"
where pokemon_id is not null
group by pokemon_id
having count(*) > 1


