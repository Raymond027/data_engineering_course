
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  select *
from "pokemon_db"."analytics_staging"."stg_pokemon"

where hp < 0
   or attack < 0
   or defense < 0
   or speed < 0
  
  
      
    ) dbt_internal_test