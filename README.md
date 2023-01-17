# Count-on-it

* Primary goal is to practice being able to use Vite and Svelte for front end and do back end unit testing (just for python really) at a not complete shit level. May also be good to try to practice api requests for outside the app, but not a primary goal.

* For the app itself - Ideally I'd want something that would be powerful enough to basically track progress for a movie/show/book etc, producing a list and also be flexiable enough that it could also be used to nicely track simple events like how many times someone finishes their cup of water, goes for a walk, etc

* I think tracking events is what I'll start with as a MVP and possibly look at doing the more ideal/powerful stuff from there if I'm still going strong

### Tables
#### Counter table
  * Going to do it all on one big table. This helps alivate the entire issue making column names match between tables for counters so that the tables. Instead in the view I'll allow users to save the name as something other than what it's actually called. So you'd have a generic name column for your books, movies, shows, etc, but then when you're viewing it under a view called something like "anime", the name will appear as "Anime name" or something instead.
  * Need to think about how I would do something like a "count" on the counter. Should it be an integer right on the table, or should it be a calculated field from the log produced by the counter.
  
#### Log table
  * This will just be the output of the counters basically. It would have the same columns, and the views would work the same
  
#### Views table
  * This will be some properties like the ID, name, created date, etc. Then a lot of it will be the query the user saves.

#### Link table
  * Used to link views to corrisponding counters, columns, filters, user's query, etc. I need to think about if I need multiple link tables for this, or just the one.
  
  ![image](https://user-images.githubusercontent.com/85081861/212760670-c2276661-d030-4af4-b8c8-3460e4b4e3a0.png)
  ```
  SELECT Counters.*
  FROM Counters
  JOIN CountersInView ON CountersInView.CounterID = Counters.ID
  JOIN Views ON Views.ID = CountersInView.ViewID
  WHERE Views.Name = 'anime' AND Counter.Score > 8;
  ```

### Header
  * Drop down to say if you want to look at the counters, logs, or both
  * Filters, let's you do basic filters on a row based on a column like "less than x"
  * Columns, let's you select which columns to view
  * Export, exports to csv
  * Sort, as basic as filtering
  * SQL, for the advanced

### Main screen section that shows the currently toggled visible counters either -
  * As the counters themselves
  * A spreadsheet style log of counter clicks
  * Both

### Side bar
  * "Views" which is just saved views
      * Would mostly just save if you're looking at log or counter view and any relevant header info like filters, columns, sort.
      * Might be worth considering have nested views. So that someone could have "stories" and then "books", "TV", "Movies" under that.
  * Possibly have a "Tables" section, this would only be if I went with the idea that there would be different tables that you attach counters to
  * User created sections (So I imagine this is like how in Asana a project needs to be in a team, but can be in multiple porfolios, which here is views)
      * Maybe one premade section called "counters" or something just to start. Editable and deletable.
      * Used to group counters
      * Clicking the counter should pull up a view that's just the counter and the logs of clicks from that counter. Like how clicking it in Asana brings you to a default saved view of the project
      * Able to toogle the entire section on or off
      
      
Example 
![PXL_20230112_033520178](https://user-images.githubusercontent.com/85081861/211969887-edb5ce13-9ef9-4cfa-9b76-d8bd4656699e.jpg)
