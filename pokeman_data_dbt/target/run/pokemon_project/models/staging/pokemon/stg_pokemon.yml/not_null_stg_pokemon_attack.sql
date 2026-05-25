
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select attack
from "pokemon_db"."analytics_staging"."stg_pokemon"
where attack is null



  
  
      
    ) dbt_internal_test