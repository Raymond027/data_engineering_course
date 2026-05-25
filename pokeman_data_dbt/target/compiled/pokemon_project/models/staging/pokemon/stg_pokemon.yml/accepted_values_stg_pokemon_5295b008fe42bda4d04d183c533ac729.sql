
    
    

with all_values as (

    select
        generation as value_field,
        count(*) as n_records

    from "pokemon_db"."analytics_staging"."stg_pokemon"
    group by generation

)

select *
from all_values
where value_field not in (
    '1','2','3','4','5','6','7','8','9'
)


