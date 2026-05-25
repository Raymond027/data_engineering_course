
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select is_legendary
from "pokemon_db"."analytics_staging"."stg_pokemon"
where is_legendary is null



  
  
      
    ) dbt_internal_test